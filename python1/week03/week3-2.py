name = "Kim"
age = 20
a =10
b= 5
pi = 3.141592
score = 75
money = 1234567
year = 2025
month = 3
day = 14

print(f"이름 : {name}, 나이 :{age}")
# 계산식
print(f"{a} + {b} = {a+b}")
# 소수점 자릿수
print(f"원주율(둘째자리) : {pi:.2f}")

print(f"오른쪽 정렬 | {age:5}|")
print(f"왼쪽 정렬 | {age<5}|")
print(f"가운데 정렬 | {age^5}|")

print(f"번호:{b:03}")
print(f"금액 : {money:,}원")

print(f"시험 결과: {'합격' if score >= 60 else'불합격'}")

print(f"날짜 : {year}-{month:02}-{day:02}")