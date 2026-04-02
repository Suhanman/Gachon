price1 = int(input("상품 1 가격:"))
price2 = int(input("상품 2 가격:"))
price3 = int(input("상품 3 가격:"))
price4 = int(input("상품 4 가격:"))

tax1 = price1 * 0.1
tax2 = price2 * 0.1
tax3 = price3 * 0.1
tax4 = price4 * 0.1

total_tax = tax1 + tax2 + tax3 + tax4
total_price = price1 + price2 + price3 + price4

print("총 세금 :", total_tax)
print("총 금액 :", total_price)

