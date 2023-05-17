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
"""
for i in range(1, 100):
    print(i)
