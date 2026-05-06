nums = [1,2,3]

nums.insert(1,10)
print("삽입 후:", nums)
nums.append(4)
print("추가 후:", nums)
nums.append([5,6])
print("추가 후:", nums)

last = nums.pop()
print("pop으로 반환된 값:", last)
print("삭제 후:", nums)
nums.pop(0)
print("삭제 후:", nums)
nums.remove(3)
print("삭제 후:", nums)

idx = nums.index(2)
cnt = nums.count(5)

print("값의 2의 인덱스:", idx)
print("값의 5의 개수:", cnt)