import os
import re
import time
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote


uc.Chrome.__del__ = lambda self: None


def get_driver(version=None):
    options = uc.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=ko-KR")
    # 창을 보고 싶지 않다면 headless=True로 변경
    return uc.Chrome(options=options, version_main=version, headless=False)

def crawl_google_images(keyword: str, max_images: int = 20):
    save_dir = keyword.replace(" ", "_")
    os.makedirs(save_dir, exist_ok=True)

    print(f"[*] '{keyword}' 수집 시작...")
    driver = None

    try:
        try:
            driver = get_driver()
        except:
            driver = get_driver(version=146)

        search_url = f"https://www.google.com/search?q={quote(keyword)}&tbm=isch"
        driver.get(search_url)
        time.sleep(3)

        # 1. 스크롤
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(3):
            body.send_keys(Keys.END)
            time.sleep(1.5)

        # 2. 이미지 URL 추출
        page_source = driver.page_source
        img_urls = re.findall(r'\["(https?://[^"]+\.(?:jpg|jpeg|png))",\s?\d+,\s?\d+\]', page_source)
        img_urls = list(dict.fromkeys(img_urls))
        print(f"[*] 총 {len(img_urls)}개의 후보 이미지 발견")

        # 3. 다운로드
        saved = 0
        session = requests.Session()
        for url in img_urls:
            if saved >= max_images: break
            try:
                res = session.get(url, timeout=5)
                if res.status_code == 200 and len(res.content) > 5000:
                    ext = ".png" if ".png" in url.lower() else ".jpg"
                    with open(os.path.join(save_dir, f"{saved+1}{ext}"), "wb") as f:
                        f.write(res.content)
                    print(f"  ({saved+1}/{max_images}) 성공")
                    saved += 1
            except: continue

    except Exception as e:
        print(f"[ 에러 ] {e}")

    finally:
        if driver:
            try:
                print("[*] 브라우저 종료 중...")
                driver.quit()
            except:
                pass
            driver = None # 참조 제거
        print("[ 완료 ] 모든 작업이 끝났습니다.")

if __name__ == "__main__":
    kw = input("검색 키워드: ").strip()
    cnt = input("수량 (기본 20): ").strip()
    cnt = int(cnt) if cnt.isdigit() else 20
    if kw: crawl_google_images(kw, cnt)