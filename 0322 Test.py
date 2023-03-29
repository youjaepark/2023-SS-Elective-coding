국어 = 80
영어 = 75 
수학 = 55 
print((국어 + 영어 + 수학) /3)

n = 13
print(n%2 == 1)

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print(pin[7])

a = "a:b:c:d"
b = a.replace(':','#')
print(b)

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a = ["life","is","too","short"]
result = ' '.join(a)
print(result)
 
a = (1,2,3)
a += (4,)
print(a)