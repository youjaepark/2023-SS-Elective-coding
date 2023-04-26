coffee = 10
while coffee >0:
    money = int(input("돈을 입력하세요: "))
    if money >= 300:
        print("커피 나옵니다.")
        coffee -= 1 
        print(f"남음 커피 재고량은 {coffee} 입니다.")
        print(f"잔돈은 {money-300} 입니다.")
    else: 
        print("돈이 부족합니다")
print("커피가 다 떨어졌습니다.")