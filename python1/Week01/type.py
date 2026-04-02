x = 10
y = 3.14
z = "python"
k = True
print(type(x)) # int
print(type(y))
print(type(z))
print(type(k))

# 1. 사용자 입력(문자열)
num1 = input("첫 번째 숫자를 입력하세요.")
num2 = input("두 번째 숫자를 입력하세요")
print("입력값 자료형: ", type(num1), type(num2))

#2. 문자열 -> 정수 변환
num1 = int(num1)
num2 = int(num2)

#3. 계산
sum_value = num1 + num2
print(" 두수의 합 :", sum_value)

#4. 자동 형 변환(int + float)
a = 10
b= 3.5
result = a+ b
print("자동 형 변환 결과: ", result)
print("결과 자료형: ", type(result))

# 5. 숫자 -> 문자열 전환
age = 20
message = "나이는" + str(age) + "살 입니다."
print(message)
