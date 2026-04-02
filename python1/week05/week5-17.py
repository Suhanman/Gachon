age = int(input("나이를 입력하세요:"))

if age < 18:
    print("청소년 요금 적용(기본 5000원)")
    if age < 10:
        print("추가 할인 적용 : 50% 할인(2500원)")
    else:
        print("기본 청소년 요금 적용(5000원)")
elif age >65:
    print("노인 할인 요금 적용(30% 할인)")

else:
    print("일반 요금 적용(10000원)")