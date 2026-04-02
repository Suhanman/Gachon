price = int(input("상품 가격을 입력하세요:"))

if price > 20000:
    shipping_cost = 0
else:
    shipping_cost = 3000

print(f'배송비는 {shipping_cost}원입니다')