scores = [
    [70,80,90],
    [60,70,85],
    [88,92,100],
]

for row in scores:
    max_val = row[0]

    for s in row:
        if s>max_val:
            max_val = s

    print("최댓값:", max_val)