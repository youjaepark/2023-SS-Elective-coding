"""
a = "Life is too short, you need python."

if "wife" in a:
    print("print")
elif "python" in a and "you" in a:
    print("python")
elif "shirt" in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

count = 1
sum = 0
while count <= 1000:
    if count % 3 ==0:
        sum += count
    count+=1
print(sum)

row = 5
while row >= 1:
    print("*" * row)
    row -= 1

num1 = int(input("첫번째 정수를 입력해주세요: "))
num2 = int(input("두번째 정수를 입력해주세요: "))
if num1 > num2:
    print("Yes")
else:
    print("No")
    
def cal():
    a = int(input("첫번째 숫자를 입력하세요: "))
    b = int(input("두번째 숫자를 입력하세요: "))
    i = input("기호를 입력하세요: ")
    if i == "+":
        return a + b
    if i == "-":
        return a - b
    if i == "*":
        return a * b
    if i == "/":
        return a / b
    if i == "%":
        return a % b


print(cal())

def three(a):
    if a % 3 == 0:
        print("3의 배수 입니다.")
    else:
        print("3의 배수가 아닙니다.")
 
i = int(input("숫자를 입력하세요: "))
three(i)
"""

h = int(input("키를 입력하세요: "))
w = int(input("몸무게를 입력하세요: "))


def bmi():
    print(round(int(w) / (int(h) / 100) ** 2, 2))


bmi()
