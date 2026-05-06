nums1 = [1,-2,3,-4,5]

for x in nums1:
    if x < 0:
        continue
    print(x, end=" ")

print("\n")

###############################

nums2 = [10,20,0,30]

print("0에서 중단:")
for x in nums2:
    if x == 0:
        break
