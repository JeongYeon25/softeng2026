import tkinter as tk

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_prime():
    try:
        num = int(entry.get())
        if is_prime(num):
            result_label.config(text=f"{num}은(는) 소수입니다.")
        else:
            result_label.config(text=f"{num}은(는) 소수가 아닙니다.")
    except ValueError:
        result_label.config(text="유효한 숫자를 입력하세요.")

def blink():
    current_color = button.cget('bg')
    if current_color == 'misty rose':
        button.config(bg='pink')
    else:
        button.config(bg='misty rose')
    root.after(500, blink)

root = tk.Tk()
root.title("소수 판별기")
root.configure(bg='alice blue')

tk.Label(root, text="숫자를 입력하세요:", bg='alice blue', font=('TkDefaultFont', 10, 'bold')).pack()

entry = tk.Entry(root, bg='alice blue')
entry.pack()

button = tk.Button(root, text="판별", command=check_prime, bg='misty rose')
button.pack()

result_label = tk.Label(root, text="", bg='alice blue')
result_label.pack()

blink()
root.mainloop()