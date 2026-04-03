import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

def crawl_google_images(keyword: str, max_images: int = 20, save_dir: str = None):
    if save_dir is None:
        save_dir = keyword.replace(" ", "_")

    os.makedirs(save_dir, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)

    try:
        search_url = f"https://www.google.com/search?q={requests.utils.quote(keyword)}&tbm=isch"
        driver.get(search_url)

        # 스크롤하여 이미지 더 로드
        for _ in range(3):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(1.5)

        # 이미지 썸네일 요소 수집
        thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")
        print(f"[*] 발견된 이미지 수: {len(thumbnails)}")

        saved = 0
        for i, thumb in enumerate(thumbnails):
            if saved >= max_images:
                break

            try:
                driver.execute_script("arguments[0].click();", thumb)
                time.sleep(1)

                # 고화질 이미지 URL 추출
                full_imgs = driver.find_elements(
                    By.CSS_SELECTOR, "img.iPVvYb, img.r48jcc"
                )
                img_url = None
                for img in full_imgs:
                    src = img.get_attribute("src")
                    if src and src.startswith("http") and "gstatic" not in src:
                        img_url = src
                        break

                # 고화질 이미지를 찾지 못하면 썸네일 src 사용
                if not img_url:
                    img_url = thumb.get_attribute("src")

                if not img_url or img_url.startswith("data:"):
                    continue

                ext = os.path.splitext(urlparse(img_url).path)[-1].lower()
                if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
                    ext = ".jpg"

                file_path = os.path.join(save_dir, f"{keyword}_{saved+1}{ext}")
                response = requests.get(img_url, timeout=5, headers={
                    "User-Agent": "Mozilla/5.0"
                })
                if response.status_code == 200:
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"  [{saved+1}] 저장 완료: {file_path}")
                    saved += 1

            except Exception as e:
                print(f"  [!] 이미지 {i+1} 처리 중 오류: {e}")
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
