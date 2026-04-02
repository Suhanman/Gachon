score = int(input("점수를 입력하세요: "))

if score >= 90:
    if score >=95:
        print("A + 학점")
    else:
        print("A 학점")

elif score >= 80:
    if score >=85:
        print("B + 학점")
    else :
        print("B 학점")

else :
    print("C 학점 이하에요")