scores = [70,72,68,75,80,78,85]

count = 0
for i in range(1, len(scores)):
    if scores[i] > scores[i-1]:
        count += 1

print("증가한 횟수:", count)
