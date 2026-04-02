correct_id="admin"
correct_pw="1234"

user_id = input("아이디를 입력하세요:")

if user_id == correct_id:
    user_pw = input("비밀번호를 입력하세요: ")
    if user_pw == correct_pw:
        print("로그인의 성공")
    else:
        print("틀린 비밀번호 입니다.")
else:
    print("아이디가 존재하지 않습니다.")