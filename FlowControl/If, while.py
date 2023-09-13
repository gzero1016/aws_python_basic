username = "bbb"
password = "12344"

if username == "aaa" and password == "1234":
    print("참")
else:
    print("거짓")

print()

if username == "aaa":
    print("username이 같음")
elif password == "1234":
    print("password가 같음")
else:
    print("둘다 다름")

print()

while True:
    menu = input("메뉴입력:")
    if menu == "q":
        break

    print("while 반복")
