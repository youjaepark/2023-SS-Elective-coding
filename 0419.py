while True:
    money = int(input("돈을 입력하세요"))
    if money >= 4500:
        ans= input("모든 물건을 살수 있습니다. 무엇을 사시겠습니까? [콜라, 초콜릿, 컵밥]")
        if ans =="콜라":
            print(f"콜라를 구매했습니다. 남은 돈은 {money-1500} 원 입니다.")
        if ans =="초콜릿":
            print(f"초콜릿을 구매했습니다. 남은 돈은 {money-2800} 원 입니다.")
        if ans == "컵밥":
            print(f"컵밥을 구매했습니다. 남은 돈은 {money-4500} 원 입니다.")
    elif money >= 2800:
        ans= input("콜라와 초콜릿 을 살수 있습니다. 무엇을 사시겠습니까? [콜라, 초콜릿]")
        if ans =="콜라":
            print(f"콜라를 구매했습니다. 남은 돈은 {money-1500} 원 입니다.")
        if ans =="초콜릿":
            print(f"초콜릿을 구매했습니다. 남은 돈은 {money-2800} 원 입니다.")
    elif money >= 1500:
        ans= input("콜라만 살수 있습니다.구매하시겠습니까? ")
        if ans =="콜라":
            print(f"콜라를 구매했습니다. 남은 돈은 {money-1500} 원 입니다.")
    else:
        print("돈이 부족합니다.")
    
        

