nums = [5,12,7,20,3,17]

for i in range(len(nums)):
    if nums[i] < 10:
        nums[i] = 0
        print("수정된 위치",i)

print(nums)