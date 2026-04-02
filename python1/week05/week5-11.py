country = input('배송지는 korea와 china만 가능:')
price = int(input('상품의 가격을 입력하세요:'))

if country == 'korea' and price >= 20000:
    shipping_cost = 0

elif country == 'korea':
    shipping_cost = 3000

elif country == 'china' and price >=100000:
    shipping_cost = 0

elif country == 'china':
    shipping_cost = 8000

else:
    print("지원하지 않는 국가입니다.")
    shipping_cost = 0

print(f"{country}로의 배송비는 {shipping_cost}원 입니다.")