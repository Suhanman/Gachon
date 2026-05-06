students = (
    ("Kim", 85, 90, 78),
    ("Lee", 92, 88, 95),
    ("Park", 70, 65, 80),
    ("Choi", 60, 75, 68),
    ("Jung", 95, 98, 100)
)

max_avg = 0                 # 최고 평균
top_student = ""         # 최고 평균 학생
total_avg_sum = 0         # 전체 평균

# 1. 튜플 언패킹

for name, s1, s2, s3 in students:
    total = s1 + s2 + s3
    avg = total / 3

    # 3. 학점계산
    if avg >= 90: grade = "A"
    elif avg >= 80: grade = "B"
    elif avg >= 70: grade = "C"
    elif avg >= 60: grade = "D"
    else: garde = "F"

    # 4. 최고 평균 찾기

    if avg > max_avg :
        max_avg = avg
        top_student = name

    total_avg_sum += avg    # 총 평균
    print(f"{name} → 총점: {total}, 평균: {avg:.1f}, 학점: {grade}")

# 5. 전체 평균
overall_avg = total_avg_sum / len(students)

print("최고 평균 학생")
print(f"{top_student} ({max_avg:.1f})")
print("전체 평균")
print(f"{overall_avg:.1f}")
