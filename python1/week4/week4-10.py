age = int(input("나이를 입력하세요"))
user_id = input("아이디를 입력하세요")
password = input("비밀번호를 입력하세요")

if age >= 19 and 6<= len(user_id) <= 12 and len(password) >=8:
    print("회원가입 성공")
else:
    print("회원가입 실패")


score = int(input("점수를 입력해주세요:"))
absence = int(input("결석 횟수를 입력해주세요:"))
if score> 100 or score <0 or absence>=3:
    print("시험 응시 불가")
else:
    print("시험 응시 가능")

hour = int(input("해당하는 시간을 입력해주세요:"))
tf = input("지금은 주말인가요?(y/n)")
if tf == "y":
    is_weekend = 1
elif tf == "n":
    is_weekend = 0
else:
    print("오류입니다.")
    is_weekend = None

if (hour >=22 or hour <6) and is_weekend == False:
    print("야간 할인 적용대상입니다.")
else :
    print("야간 할인 적용대상이 아닙니다.")

height = int(input("키를 입력하세요: "))
age = int(input("나이를 입력해주세요: "))
tf = input("동반자가 있나요?(y/n):")

if tf == "y":
    with_guardian = 1
elif tf == "n":
    with_guardian= 0
else:
    print("오류입니다.")
    with_guardian = None

if height > 140 and age > 12 and with_guardian == 1:
    print("입장 제한 해당없음")
else :
    print("입장제한")

tf_vip = input("vip 인가요?(y/n)")
if tf_vip == "y":
    is_vip = 1
elif tf_vip == "n":
    is_vip= 0
else:
    print("오류입니다.")
    is_vip = None

tf_coupon = input("쿠폰이 있나요? (y/n)")
if tf_coupon == "y":
    is_coupon = 1
elif tf_coupon == "n":
    is_coupon= 0
else:
    print("오류입니다.")
    is_coupon = None

price = int(input("구매 금액이 어떻게 되나요?:"))

if is_vip == 0 and is_coupon == 0 and price < 50000:
    print("할인 대상이 아닙니다.")
else:
    print("할인 대상입니다.")