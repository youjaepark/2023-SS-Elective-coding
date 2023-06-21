import random

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"


def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result


# data.txt 파일 생성
with open("data.txt", "w") as d:
    for i in range(1, 101):
        d.write(
            random_name()
            + ","
            + str(random.randrange(30, 100))
            + ","
            + str(random.randrange(100, 190))
            + "\n"
        )

# 텍스트파일 복제
with open("data.txt", "r") as d:
    data = d.read()
    with open("bmi.txt", "w") as b:
        b.write(data)


# BMI 계산
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m**2)
    return bmi


# BMI를 바탕으로 체형 판단
def get_weight_status(bmi):
    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 25:
        return "정상"
    elif 25 <= bmi < 30:
        return "과체중"
    else:
        return "비만"


# bmi.txt 파일 읽어들이기
with open("bmi.txt", "r") as file:
    lines = file.readlines()
updated_lines = []

for line in lines:
    name, weight, height = line.strip().split(",")
    height = int(height)
    weight = int(weight)
    bmi = calculate_bmi(weight, height)
    weight_status = get_weight_status(bmi)
    updated_line = f"{name},{weight},{height},{round(bmi)},{weight_status}\n"
    updated_lines.append(updated_line)

with open("bmi.txt", "w") as file:
    file.writelines(updated_lines)
