scores = [70,85,90,60,75]

avg = sum(scores)/len(scores)


count = 0
for s in scores:
    if s>=avg:
        count+=1

print(count)

