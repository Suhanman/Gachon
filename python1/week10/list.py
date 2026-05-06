## 파이썬의 자료구조

temps = [28,44,3432,32423,445435,55]

temps[0] = 30

temps[-1] = 24
print(temps)

temps = [25,31,33,35,27,26,24]

for i in range(7):
    if  temps[i] >= 30:
        temps[i] = temps[i] - 5

    print(temps)