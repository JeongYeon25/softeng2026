import tkinter as tk
from tkinter import messagebox

def check_even(n):
    return n % 2 == 0

def check_number():
    try:
        num = int(entry.get())
        if check_even(num):
            result_label.config(text=f"{num}는 짝수입니다.")
        else:
            result_label.config(text=f"{num}는 홀수입니다.")
    except ValueError:
        messagebox.showerror("오류", "숫자를 입력하세요!")

window = tk.Tk()
window.title("짝수 판별기")
window.geometry("300x200")

entry = tk.Entry(window)
entry.pack(pady=10)

btn = tk.Button(window,text="확인",bg="pink",command=check_number)
btn.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.bind("<Return>", lambda event: check_number())

window.mainloop()