age = int(input("나이를 입력하세요:"))

if age < 10:
    fee = 2500
    print("청소년 요금 + 추가 할인 적용(2500원)")

elif age <18:
    fee = 5000
    print("청소년 요금 적용(5000원)")

elif age >=65:
    fee = 7000
    print("노인 할인 요금 적용(7000원)")

else:
    fee = 10000
    print("일반 요금적용 (10000원)")