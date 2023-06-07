# data.txt 파일 생성
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


with open("C:/Users/haven06/Desktop/파이썬 고등/2023-SS-Elective-coding/data.txt", "w") as f:
    for i in range(1, 101):
        f.write(
            random_name()
            + ", "
            + str(random.randrange(30, 100))
            + ", "
            + str(random.randrange(100, 190))
            + "\n"
        )

# 텍스트파일 복제
with open("C:/Users/haven06/Desktop/파이썬 고등/2023-SS-Elective-coding/data.txt", "r") as f:
    with open(
        "C:/Users/haven06/Desktop/파이썬 고등/2023-SS-Elective-coding/bmi.txt", "w"
    ) as b:
        data = f.read()
        b.write(data)

with open("C:/Users/haven06/Desktop/파이썬 고등/2023-SS-Elective-coding/bmi.txt", "r") as b:
    while True:
        line = b.readline().split(",")
        weight = int(line[1])
        height = int(line[2][1:4])
        bmi = height / (weight**2)
