is_raining = int(input("비가 오면 1 , 아니면 0을 입력하세요"))
budget = int(input("예산을 입력하세요 : "))

if is_raining == 1:
    print("따뜻한 국물 음식 (국밥, 칼국수)")


elif is_raining == 0:
    if budget >= 10000:
        print("먹고 싶은 음식")
    else:
        print("저렴한 메뉴 (분식, 편의점 음식")

else :
    print("잘못한 입력입니다.")