employees = (
    ("Kim", 2500000, 300000),
    ("Lee", 2200000, 200000),
    ("Park", 1800000, 150000),
    ("Choi", 3000000, 500000),
    ("Jung", 2000000, 100000)
)

print("📊 급여 계산 결과\n")

for name, base, bonus in employees:   # 1. 튜플 언패킹
    # 2. 총급여
    total = base + bonus

    # 3. 세금 (10%)
    tax = total * 0.1

    # 4. 실수령액
    final = total -tax

    print(f"{name} → 총급여: {total:,}, 세금: {int(tax):,}, 실수령액: {final:,}")
