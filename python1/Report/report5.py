system_A = ("kim", "lee", "park", "choi", "jung")
system_B = ("lee", "park", "han", "choi", "song")

# 1. 튜플 → 집합 변환
set_A = set(system_A)
set_B = set(system_B)

# 2. 교집합 (공통 사용자)
common = set_A & set_B

# 3. A에는 있고 B에는 없는 사용자
only_A = set_A - set_B

# 4. B에는 있고 A에는 없는 사용자
only_B = set_B - set_A

# 5. 정렬
common = sorted(common)
only_A = sorted(only_A)
only_B = sorted(only_B)

# 출력
print("📊 사용자 분석 결과\n")

print("공통 사용자:", common)
print("A에만 있는 사용자:", only_A)
print("B에만 있는 사용자:", only_B)
