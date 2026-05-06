products = [
    ["노트북", 1200000, 3],
    ["마우스", 25000, 20],
    ["키보드", 45000, 15],
    ["모니터", 300000, 5],
    ["USB", 12000, 50]
]

max_qty = 0
max_product = ""

for p in products:
    name = p[0]
    price = p[1]
    qty = p[2]

    # 1. 매출액 계산
    sales = price * qty

    # 2. 최대 판매 수량 찾기

    if qty > max_qty:
        max_product = name
        max_qty = qty

    # 3. 등급 부여
    if sales >= 1000000 :
        grade = "우수"
    elif sales >= 500000 :
        grade = "보통"
    else :
        grade = "주의"



    print(f"{name} → 매출액: {sales:,}원 / 등급: {grade}")

# 결과 출력
print("\n 판매 수량 1위 상품")
print(f"{max_product} ({max_qty}개 판매)")
