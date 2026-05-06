students = [
    ["Kim", 85, 90, 78],           # 이름 + 3과목 점수
    ["Lee", 92, 88, 95],
    ["Park", 70, 65, 80],
    ["Choi", 60, 75, 68],
    ["Jung", 95, 98, 100]
]

total_avg_sum = 0                # 전체 평균 계산용 누적 변수
count = 0                            # 학생 수

for s in students:                  # 각 학생 반복
    name = s[0]                     # 이름 추출
    total = s[1] + s[2] + s[3]    # 총점 계산
    avg = total / 3                 # 평균 계산

    if avg >= 90:          grade = "A"     # 학점 계산
    elif avg >= 80:        grade = "B"
    elif avg >= 70:        grade = "C"
    elif avg >= 60:        grade = "D"
    else:                      grade = "F"

    print(f"{name}\t{total}\t{avg:.1f}\t{grade}")    # 결과 출력
    total_avg_sum += avg    # 평균 누적
    count += 1                   # 학생 수 증가

# 전체 평균 계산
class_avg = total_avg_sum / count
print("-" * 40)
print(f"전체 평균: {class_avg:.1f}")

