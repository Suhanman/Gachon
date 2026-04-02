# celsius = float(input('섭씨 온도 입력:'))
# fahrenheit = (9/5) * celsius + 32
# print('섭씨',celsius, '도는 화씨', fahrenheit, '도입니다.')
#

# price = int(input("상품 가격을 입력하세요:")) # float
# discount_rate = float(input('0~1 사이 할인율을 입력해요:')) # float
#
# discount = price * discount_rate
# total = price - discount
#
# print('할인된 가격은? ', round(total), '원입니다')

# a = 10
# b = 20
# c = 30
#
# print(a,b,c)
# print(a,b,c, sep = " - ")
# print("합계: ", end = " ")
# print(a+b+c , end = " * ")
# print("출력 완료")

name = "Kim"
age = 20

# 콤마 방식 (기본 , 가장 쉬움)
print("이름 :", name, "나이:",age)

print(f"이름 :{name}, 나이 :{age}")

print("이름 : {}, 나이 : {}".format(name,age))