scores = [
    [80,70.90],
    [85,88,92],
    [80,76.90]
]

for i in range(len(scores)):
    total = 0

    for score in scores[i]:
        total += score
    avg = total / len(scores[i])

    print(f"{i+1}번 학생 평균:{avg}")