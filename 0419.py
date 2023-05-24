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
    """


def add(a, b, c):
    return a + b + c


print(add(1, 2, 3))
