mid = int(input ("중간고사 점수:"))
fin = int(input("기말고사 점수:"))
att = int(input("출석 점수:"))
rep = int(input("레포트 점수:"))

#데이터 처리
total = mid + fin + att +rep
if total>= 90:
    grade = "A"
elif total >= 80:
    grade ="B"
elif total >= 70:
    grade ="C"
elif total >= 60:
    grade ="D"
else :
    grade = "F"

# 결과 출력
print(f"총점 :{total}, 학점 : {grade}")
