count = 0
total = 0

for i in range(1,101):
    if i%3 == 0 and i % 5 !=0:
        count +=1
        total +=i

    print("개수:",count)
    print("합",total)