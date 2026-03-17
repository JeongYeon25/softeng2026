import tkinter as tk

def c2f(c):
    return c * 9/5 + 32

def f2c(f):
    return (f - 32) * 5/9

def convert():
    try:
        temp = float(entry.get())
        if choice.get() == "℃":
            result = c2f(temp)
            result_label.config(text=f"{result:.2f} ℉")
        elif choice.get() == "℉":
            result = f2c(temp)
            result_label.config(text=f"{result:.2f} ℃")
        else:
            result_label.config(text="단위를 선택하세요.")
    except ValueError:
        result_label.config(text="유효한 숫자를 입력하세요.")

root = tk.Tk()
root.title("온도 변환기")
root.configure(bg='lavender')
root.geometry("400x300")

choice = tk.StringVar()

title_label = tk.Label(root, text="온도 변환기", bg='lavender', font=('Verdana', 16, 'bold'), fg='black')
title_label.pack(pady=20)

frame = tk.Frame(root, bg='lavender')
frame.pack(pady=10)

tk.Radiobutton(frame, text="℃ to ℉", variable=choice, value="℃", bg='lavender', font=('Verdana', 12), fg='black').pack(side=tk.LEFT, padx=20)
tk.Radiobutton(frame, text="℉ to ℃", variable=choice, value="℉", bg='lavender', font=('Verdana', 12), fg='black').pack(side=tk.LEFT, padx=20)

entry_label = tk.Label(root, text="온도를 입력하세요:", bg='lavender', font=('Verdana', 12), fg='black')
entry_label.pack(pady=5)

entry = tk.Entry(root, bg='white', font=('Verdana', 12))
entry.pack(pady=5)

convert_button = tk.Button(root, text="변환", command=convert, bg='light blue', font=('Verdana', 12), fg='black', relief='raised', bd=3)
convert_button.pack(pady=20)

result_label = tk.Label(root, text="", bg='lavender', font=('Verdana', 12), fg='black')
result_label.pack(pady=10)

root.mainloop()