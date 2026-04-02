pencil_price = 500
note_price = 1200
eraser_price = 700


pencil = int(input("연필 갯수: "))
note = int(input("공책 개수: "))
eraser = int(input("지우개 개수: "))

sum = pencil_price * pencil + note_price * note + eraser_price * eraser

print("총 금액", sum)