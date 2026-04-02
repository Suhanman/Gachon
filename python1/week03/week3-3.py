salary = int(input("월급 입력:"))
bonus = int(input("보너스 입력:"))

income_tax_rate = 0.12
pension_rate = 0.045
health_rate = 0.035


total_income = salary + bonus

income_tax = total_income * income_tax_rate
pension = total_income * pension_rate
health_rate = total_income * health_rate

total_tax = income_tax + pension + health_rate
net_income = total_income - total_tax

print("\n[급여 계산결과]")
print("총소득 :", total_income, "원")

print("소득세", "국민연금", "건강보험료", sep=" / ")
print(f"소득세:{income_tax:,.0f}원")
print(f"국민연금:{pension:,.0f}원")
print(f"건강보험료:{health_rate:,.0f}원")

print("총 세금", end =" ")
print(f"{total_tax:,.0f}원")

print(f"실수령액 : {net_income:,.0f}원")