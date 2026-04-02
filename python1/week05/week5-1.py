speed = int(input('속도를 입력하세요:'))

if speed >= 70:
    print('매우 위험한과속입니다')
    print('속도를 줄이세요')
if speed >= 50 and speed <70:
    print('과속입니다. 속도를 줄이세요')

if speed >= 30 and speed <50:
    print('주의 속도가 높습니다.')
if speed <30 :
    print('정상이에요')

print('프로그램 종료 예정')