employees = [
    ["Kim", 2500000, 300000, 92],
    ["Lee", 2200000, 200000, 85],
    ["Park", 1800000, 150000, 70],
    ["Choi", 3000000, 500000, 95],
]

for e in employees:
    name = e[0]
    base = e[1]
    bonus = e[2]
    score = e[3]

    # 각 직원의 총급여를 계산하시오.
    total = base + bonus
    # 총급여의 10%를 세금으로 계산하시오.
    tax = total * 0.1
    # 실수령액을 계산하시오.
    final = total - tax
    # 근무평가 점수에 따라 성과 등급을 부여하시오.
    if score >= 90 : grade = "우수"
    elif score >= 80 : grade = "양호"
    elif score >= 70 : grade = "보통"
    else : grade = "개선필요"

    print(f"{name} → 총급여: {total:,}원, 세금: {int(tax):,}원, 실수령액: {final:,}원, 등급: {grade}")
