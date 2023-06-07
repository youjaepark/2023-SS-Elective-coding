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

h = int(input("키를 입력하세요: "))
w = int(input("몸무게를 입력하세요: "))


def bmi():
    print(round(int(w) / (int(h) / 100) ** 2, 2))

bmi()

def say():
    return "2023년 5월 31일 수요일"

def sub(a, b):
    print(f"{a} 와 {b} 의 차는 {a-b} 입니다.")

def sum(a, b):
    return (a + b) / 2

def avg(*args):
    result = 0
    for i in args:
        result += i
    result = result / len(args)
    return result

def nameage(n, a):
    print({n: a})


name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
nameage(name, age)

def my(name, age, man=True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {age}살입니다.")
    if man:
        print("남자")
    else:
        print("여자")

my("박유재", 29, True)

f = open("C:/Users/haven06/Desktop/파이썬 고등/2023-SS-Elective-coding/테스트.txt", "w")

for i in range(2, 16):
    for j in range(1, 10):
        data = f"{i} x {j} = {i*j}\n"
        f.write(data)
    f.write("\n")
f.close()
f = open("C:/Users/haven06/Desktop/파이썬 고등/2023-SS-Elective-coding/테스트.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

with open("C:/Users/haven06/Desktop/파이썬 고등/2023-SS-Elective-coding/테스트.txt", "w") as f:
    f.write()

def is_odd(a):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")

is_odd(10)
"""
