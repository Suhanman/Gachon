

employees=[
    ["김창복", 250000, 1],
    ["이영희", 180000, 3],
    ["박민수", 320000, 2]
]


for emp in employees:
    name = emp[0]
    salary = emp[1]
    grade = emp[2]



    if grade == 1: allow = 300000
    elif grade == 2: allow = 200000
    elif grade == 3: allow = 150000
    elif grade == 4: allow = 100000
    elif grade == 5: allow = 50000
    else:
        print("잘못된 직급 코드입니다.")
        allow = 0

    total = salary + allow

    if total >=300000: tax_rate =0.10
    elif total >=200000: tax_rate =0.05
    else:   tax_rate = 0.03
    tax = int(total*tax_rate)
    net = total - tax


    print(f"{name}->본봉:{salary}, 수당 : {allow}, 총급여:{total}, 세금:{tax}, 실수령액:{net}")
