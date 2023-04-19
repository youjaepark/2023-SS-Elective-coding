# prompt = """
# 1. ADD
# 2. DEL
# 3. UPDATE
# 4. EXIT
# """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input("ENTER NUMBER: "))
#     if number == 1:
#         print("데이터를 추가합니다.")
#     elif number == 2:
#         print("데이터를 삭제합니다.")
#     elif number == 3:
#         print("데이터를 수정합니다.")
#     elif number == 4:
#         print("프로그램에서 나갑니다.")

coffee = 10
money = 5000
while (coffee >= 0 and money >= 100):
    print("돈을 받았으니 커피를 드리겠습니다.")
    print(f"남은 커피는 {coffee} 입니다. 잔액은 {money} 입니다")
    if coffee == 0:
        print("커피가 떨어졌습니다")
    coffee -= 1
    money -= 100
