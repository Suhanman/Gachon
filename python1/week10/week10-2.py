a = [10,20,30,40]

print("값 기준 순회")
for x in a:
    print(x)

print("\n인덱스 기준의 순회")
for i in range(len(a)):
    print(i,a[i])

print("\n인덱스 + 조건의 처리")
nums = [5,12,7,20,3]

for i in range(len(nums)):
    if nums[i] >= 10:
        print("인덱스",i,"값",nums[i])