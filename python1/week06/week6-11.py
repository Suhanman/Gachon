max_val = None

for i in range(5):
    num = int(input("정수 입력:"))

    if num >= 50:
        if max_val is None or num > max_val:
            max_val = num

print("50 이상 수 중 최댓값: ", max_val)