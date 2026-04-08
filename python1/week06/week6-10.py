even_sum = 0
odd_count = 0

for i in range(1,11):
    if i % 2 == 0:
        even_sum +=i
    else:
        odd_count += 1

    print("짝수의 합:", even_sum)
    print("홀수의 개수:", even_sum)