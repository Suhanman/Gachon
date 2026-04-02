salary = int(input("본봉을 입력해주시오:"))

grade = int(input("직급 코드를 입력해주시오(1~5):"))


if grade == 1:
    value = 300000
elif grade == 2:
    value = 200000
elif grade == 3:
    value = 150000
elif grade == 4:
    value = 100000
elif grade == 5:
    value = 50000
else :
    value = False

sum = salary + value

print("----총 급여------")

if value != False:
    print(sum)

elif value == False:
    print("직급코드오류")



if sum >= 3000000:
    tax_ratio = 10
elif 2000000 <= sum < 3000000:
    tax_ratio = 5
else :
    tax_ratio = 3

tax = sum * (tax_ratio / 100)
real_money = sum - tax

print("---출력---")

print(f"본봉: {salary}")
print(f"수당: {value}")
print(f"총급여: {sum}")
print(f"세금: {tax}")
print(f"실수령액: {real_money}")