import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("음료주문")
window.geometry("400x500")

frame1 = tk.Frame(window)
frame1.pack()

price = {"커피": 3500, "라떼": 4000, "스무디": 4500, "티": 3000}
order = []
sum = 0


def add(item):
    global sum

    if item not in price:
        print("음료가 없습니다")
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    textarea.insert(tk.INSERT, item + "")
    label1["text"] = "금액: " + str(sum) + "원"


def btn_exit():
    msgbox = tk.messagebox.askquestion("확인", "주문을 마치겠습니까?")
    if msgbox == "yes":
        exit()


tk.Button(frame1, text="커피", command=lambda: add("커피"), width=10, height=2).grid(
    row=0, column=0
)
tk.Button(frame1, text="라떼", command=lambda: add("라떼"), width=10, height=2).grid(
    row=0, column=1
)
tk.Button(frame1, text="스무디", command=lambda: add("스무디"), width=10, height=2).grid(
    row=2, column=0
)
tk.Button(frame1, text="티", command=lambda: add("티"), width=10, height=2).grid(
    row=2, column=1
)
tk.Button(frame1, text="exit", command=lambda: btn_exit(), width=10, height=2).grid(
    row=4, column=1
)

label1 = tk.Label(window, text="금액: 0원", width=100, height=2, fg="blue")
label1.pack()

textarea = tk.Text(window)
textarea.pack()

window.mainloop()
