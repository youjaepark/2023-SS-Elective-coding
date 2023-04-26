while True:
    money = int(input("돈을 입력하세요: "))
    if money >= 4500:
        print("컵밥")
        print(f"잔돈은 {money-4500} 원 입니다.")
    elif money >= 2800:
        print("초콜렛")
        print(f"잔돈은 {money-2800} 원 입니다.")
    elif money >= 1500:
        print("제로 콜라")
        print(f"잔돈은 {money-1500} 원 입니다.")          
    else: 
        print("돈이 부족합니다")
