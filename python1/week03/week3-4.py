text = "Hello Python Programming"

print("문자열 길이:" , len(text))

print("대문자:" , text.upper())

print("소문자:" , text.lower())

print("Python 위치:" , text.find("Python"))

print("문자열 변경:" , text.replace("Python", "World"))

words = text.split()
print("문자열 분리:", words)
print("공백 제거:", text.strip())