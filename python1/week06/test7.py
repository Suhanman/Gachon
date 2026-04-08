

students=[
    ["김창복", 70,80,90],
    ["이영희", 60,75,85],
    ["박민수", 88,92,100]
]

for info in students:
    name = info[0]
    socre1 = info[1]
    score2 = info[2]
    score3 = info[3]

    total  = 0

    for count in range(1,4):
        total += info[count]

    avg = total / 3

    if avg >= 90: grade = "A"
    elif avg >=80: grade = "B"
    elif avg >=70: grade = "C"
    elif avg >=60: grade = "D"
    else : "F"

    print(f"학생이름 : {name}, 평균 : {avg}, 학점 :{grade}")

