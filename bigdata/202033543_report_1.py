"""
Google Play Store Review Crawler
결과물: CSV 파일로 저장
사용 라이브러리: google-play-scraper
설치: pip install google-play-scraper
"""

import csv
import time
from datetime import datetime
from google_play_scraper import reviews, Sort


# ── 설정 ──────────────────────────────────────────────────────────────────────
APP_ID = "com.kakao.talk"          # 크롤링할 앱 패키지명
LANG = "ko"                        # 리뷰 언어
COUNTRY = "kr"                     # 국가 코드
COUNT = 500                        # 수집할 리뷰 수
SORT = Sort.NEWEST                 # 정렬 기준: NEWEST / MOST_RELEVANT
OUTPUT_FILE = "play_reviews.csv"   # 저장할 CSV 파일명
# ─────────────────────────────────────────────────────────────────────────────


def fetch_reviews(app_id: str, lang: str, country: str, count: int, sort) -> list[dict]:
    """Google Play Store 리뷰를 수집하여 리스트로 반환."""
    all_reviews = []
    continuation_token = None
    batch_size = 200  # 1회 요청당 최대 200개

    print(f"[{app_id}] 리뷰 수집 시작 (목표: {count}개)")

    while len(all_reviews) < count:
        fetch_count = min(batch_size, count - len(all_reviews))
        result, continuation_token = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=sort,
            count=fetch_count,
            continuation_token=continuation_token,
        )

        if not result:
            break

        all_reviews.extend(result)
        print(f"  수집 중... {len(all_reviews)}개")

        if continuation_token is None:
            break

        time.sleep(0.5)  # 서버 부하 방지

    print(f"  총 {len(all_reviews)}개 수집 완료")
    return all_reviews


def save_to_csv(reviews_data: list[dict], filepath: str) -> None:
    """수집된 리뷰 데이터를 CSV 파일로 저장."""
    if not reviews_data:
        print("저장할 데이터가 없습니다.")
        return

    fieldnames = [
        "reviewId",
        "userName",
        "userImage",
        "content",
        "score",           # 별점 (1~5)
        "thumbsUpCount",   # 좋아요 수
        "reviewCreatedVersion",
        "at",              # 작성일시
        "replyContent",    # 개발자 답변
        "repliedAt",       # 답변 일시
        "appVersion",
    ]

    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()

        for r in reviews_data:
            writer.writerow({
                "reviewId": r.get("reviewId", ""),
                "userName": r.get("userName", ""),
                "userImage": r.get("userImage", ""),
                "content": r.get("content", ""),
                "score": r.get("score", ""),
                "thumbsUpCount": r.get("thumbsUpCount", 0),
                "reviewCreatedVersion": r.get("reviewCreatedVersion", ""),
                "at": r.get("at", "").strftime("%Y-%m-%d %H:%M:%S") if isinstance(r.get("at"), datetime) else r.get("at", ""),
                "replyContent": r.get("replyContent", ""),
                "repliedAt": r.get("repliedAt", "").strftime("%Y-%m-%d %H:%M:%S") if isinstance(r.get("repliedAt"), datetime) else r.get("repliedAt", ""),
                "appVersion": r.get("appVersion", ""),
            })

    print(f"CSV 저장 완료 → {filepath}")


def main():
    reviews_data = fetch_reviews(APP_ID, LANG, COUNTRY, COUNT, SORT)
    save_to_csv(reviews_data, OUTPUT_FILE)


if __name__ == "__main__":
    main()
