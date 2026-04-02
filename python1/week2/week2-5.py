salary = int(input("월급 : "))
bonus = int(input("보너스 : "))

income_tax_rate = 0.12
pension_rate = 0.045
health_rate = 0.035

total_income = salary + bonus

income_tax = total_income * income_tax_rate
pension = total_income * pension_rate
health = total_income * health_rate

total_tax = income_tax + pension + health
net_income = total_income - income_tax

print("총소득 ", total_income)
print("소득세 ", income_tax)
print("국민연금 ", pension)
print("건강보험료 ", health )
print("총 세금 ", total_tax)
print("실 수령액 ", net_income)