"""
text_file_path = "text.txt"
new_text_content = ""
with open(text_file_path, "r") as f:
    body = f.read()
body = body.replace("java", "python")

with open(text_file_path, "w") as f:
    f.write(body)



class FourCal:
    def __init__(self, first, second):
        pass

    def setdata(self, first, second):
        self.first = first
        self.second = second
        print(first, second)

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
a.setdata(4, 2)
print(a.add())
"""
