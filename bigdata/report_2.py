import os
import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, quote, unquote


def extract_urls_from_source(page_source: str) -> list:
    """페이지 소스의 JSON 데이터에서 이미지 URL 추출"""
    urls = []
    seen = set()
    # Google Images는 스크립트 내 JSON에 원본 이미지 URL 포함
    pattern = r'"(https?://(?!.*gstatic)(?!.*google\.com)[^"]+\.(?:jpg|jpeg|png|gif|webp)(?:\?[^"]*)?)"'
    for url in re.findall(pattern, page_source, re.IGNORECASE):
        url = url.replace("\\u003d", "=").replace("\\u0026", "&")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def extract_urls_from_links(driver) -> list:
    """imgurl 파라미터를 포함한 링크에서 원본 이미지 URL 추출 (가장 안정적)"""
    urls = []
    seen = set()
    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='imgurl=']")
    for link in links:
        href = link.get_attribute("href") or ""
        match = re.search(r'imgurl=(https?://[^&]+)', href)
        if match:
            url = unquote(match.group(1))
            if url not in seen:
                seen.add(url)
                urls.append(url)
    return urls


def click_and_get_full_url(driver, thumb) -> str:
    """썸네일 클릭 후 고화질 이미지 URL 추출"""
    driver.execute_script("arguments[0].click();", thumb)
    time.sleep(1.5)

    # 현재 Google이 사용하는 것으로 알려진 셀렉터들
    selectors = [
        "img.iPVvYb",
        "img.r48jcc",
        "img.sFlh5c",
        "img[jsname='HiaYvf']",
        "img[jsname='kn3ccd']",
        "img[data-noaft='1']",
        ".pT0Scc img",
        ".isv-r img[src^='http']",
    ]
    for sel in selectors:
        try:
            imgs = driver.find_elements(By.CSS_SELECTOR, sel)
            for img in imgs:
                src = img.get_attribute("src") or ""
                if (src.startswith("http")
                        and "gstatic" not in src
                        and "google" not in src
                        and not src.startswith("data:")):
                    return src
        except Exception:
            continue
    return ""


def crawl_google_images(keyword: str, max_images: int = 20, save_dir: str = None):
    if save_dir is None:
        save_dir = keyword.replace(" ", "_")

    os.makedirs(save_dir, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)

    try:
        search_url = f"https://www.google.com/search?q={quote(keyword)}&tbm=isch"
        driver.get(search_url)
        time.sleep(2)

        # 스크롤하여 이미지 더 로드
        for _ in range(5):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(1.5)

        # --- 방법 1: imgurl 파라미터 링크에서 URL 추출 (가장 안정적) ---
        img_urls = extract_urls_from_links(driver)
        print(f"[방법1] 링크에서 발견된 URL: {len(img_urls)}개")

        # --- 방법 2: 페이지 소스 JSON 파싱 ---
        if len(img_urls) < max_images:
            source_urls = extract_urls_from_source(driver.page_source)
            print(f"[방법2] 소스에서 발견된 URL: {len(source_urls)}개")
            seen = set(img_urls)
            for url in source_urls:
                if url not in seen:
                    seen.add(url)
                    img_urls.append(url)

        # --- 방법 3: 썸네일 클릭으로 고화질 URL 수집 ---
        if len(img_urls) < max_images:
            thumb_selectors = ["img.YQ4gaf", "img[data-iml]", "img[data-tbnid]"]
            thumbnails = []
            for sel in thumb_selectors:
                thumbnails = driver.find_elements(By.CSS_SELECTOR, sel)
                if thumbnails:
                    break

            print(f"[방법3] 썸네일 수: {len(thumbnails)}개")
            seen = set(img_urls)
            for thumb in thumbnails[: max_images * 2]:
                if len(img_urls) >= max_images * 2:
                    break
                try:
                    url = click_and_get_full_url(driver, thumb)
                    if url and url not in seen:
                        seen.add(url)
                        img_urls.append(url)
                except Exception:
                    continue

        print(f"\n[*] 수집된 총 이미지 URL: {len(img_urls)}개")

        # --- 이미지 다운로드 ---
        saved = 0
        session = requests.Session()
        session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})

        for img_url in img_urls:
            if saved >= max_images:
                break
            try:
                ext = os.path.splitext(urlparse(img_url).path)[-1].lower()
                if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
                    ext = ".jpg"

                file_path = os.path.join(save_dir, f"{keyword.replace(' ', '_')}_{saved + 1}{ext}")
                response = session.get(img_url, timeout=8)
                if response.status_code == 200 and len(response.content) > 2000:
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"  [{saved + 1}] 저장: {file_path}")
                    saved += 1
            except Exception as e:
                print(f"  [!] 오류: {e}")
                continue

        print(f"\n총 {saved}개 이미지가 '{save_dir}/' 폴더에 저장되었습니다.")

    finally:
        driver.quit()


if __name__ == "__main__":
    keyword = input("검색 키워드를 입력하세요: ").strip()
    if not keyword:
        print("키워드를 입력해야 합니다.")
    else:
        max_count = input("다운로드할 이미지 수 (기본값 20): ").strip()
        max_count = int(max_count) if max_count.isdigit() else 20
        crawl_google_images(keyword, max_images=max_count)
