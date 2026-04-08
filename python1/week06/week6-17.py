scores = [
    [70,80,90],
    [60,70,85],
    [88,92,100],
]

for row in scores:
    for s in row:
        print(s)

for row in scores:
    total = 0
    for s in row:
        total += s
        if s>=80:
            print(s)


    print("합계:",total)