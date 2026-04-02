TAX_RATE = 0.1 # 상수 선언부

price1 = int(input("상품 1 가격 : "))
price2 = int(input("상품 2 가격 : "))
price3 = int(input("상품 3 가격 : "))
price4 = int(input("상품 4 가격 : "))

tax1 = price1 * TAX_RATE
tax2 = price2 * TAX_RATE
tax3 = price3 * TAX_RATE
tax4 = price4 * TAX_RATE


total_price = price1 + price2 + price3 +price4 # 총 상품 금액
total_tax = tax1 + tax2 + tax3 +tax4 # 총 세금 금액
total = total_price + total_tax # 총 금액

# 출력 부분 ###################
print("총 상품금액:", total_price)
print("총 세금:", total_tax)
print("총 금액:", total)