N = int(input("입력할 개수:"))
x = int(input("첫번째의 입력 값:"))

min_v =x
max_v =x

for i in range(N-1):
    x = int(input("입력 값:"))
    if x < min_v:
        minv_v = x
    if x > max_v:
        max_v = x

print("최솟값: ", min_v, "최댓값: ",max_v)