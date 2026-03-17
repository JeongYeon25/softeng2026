import tkinter as tk

def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)

def calculate():
    try:
        num = int(entry.get())
        result = fact(num)
        result_label.config(text=f"팩토리얼: {result}")
    except ValueError:
        result_label.config(text="다시 입력하세요.")

root = tk.Tk()
root.title("팩토리얼 계산기")
root.configure(bg='alice blue')

tk.Label(root, text="숫자를 입력하세요:", bg='alice blue').pack()

entry = tk.Entry(root, bg='alice blue')
entry.pack()

button = tk.Button(root, text="계산", command=calculate, bg='lavender')
button.pack()

result_label = tk.Label(root, text="", bg='alice blue')
result_label.pack()

root.mainloop()
