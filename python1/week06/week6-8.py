scores = [45, 72, 88, 55 ,90, 61]

total = 0

for score in scores:
    if score >= 60:
        total += score

print("60점 이상 합계:", total)