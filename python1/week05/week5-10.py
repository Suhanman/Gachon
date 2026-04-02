country = input('배송지는 korea와 china만 가능 : ')
price = int(input('상품의 가격을 입력하세요: '))

if country == 'korea' :
    if price >= 20000 :
        shipping_cost = 0
    else :
        shipping_cost = 3000
else :
    if price >=1000000:
        shipping_cost=0
    else :
        shipping_cost = 8000

print(f"{country}로의 배송비는 {shipping_cost}원입니다.")