correct_id="admin"
correct_pw="1234"

user_id = input("아이디를 입력하세요:")
user_pw = input("비밀번호를 입력하세요:")

if user_id == correct_id and user_pw == correct_pw:
    print("로그인 성공!")
elif user_id != correct_id:
    print("아이디가 존재하지 않습니다.")

else:
    print("비밀번호가 틀렸습니다.")