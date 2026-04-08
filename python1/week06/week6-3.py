n = int(input("정수 n 을 입력하시오:"))
sum = 0

for i in range(1, n+1):
    sum = sum + i

print(f"1부터 {n}까지의 합은 {sum}이다.")