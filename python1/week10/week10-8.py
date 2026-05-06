nums = [3,12,5,18,7,20,9]

total = 0
for n in nums:
    if n >= 10 and n % 2 ==0:
        total += n
        print(n)

print("합계:", total)