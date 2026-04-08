sum2 = 0
sum3 = 0
sum5 = 0

for i in range(1,11):
    if i % 2 ==0:
        sum2 +=i
    if i % 3 ==0:
        sum3 +=i
    if i % 5 ==0:
        sum5 +=i

print("2의 배수 합:", sum2)
print("2의 배수 합:", sum3)
print("2의 배수 합:", sum5)