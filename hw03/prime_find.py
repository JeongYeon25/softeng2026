import tkinter as tk

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes():
    try:
        num = int(entry.get())
        primes = [i for i in range(2, num + 1) if is_prime(i)]
        result_text.delete(1.0, tk.END)
        if primes:
            result_text.insert(tk.END, "소수들: " + ", ".join(map(str, primes)))
        else:
            result_text.insert(tk.END, "소수가 없습니다.")
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "유효한 숫자를 입력하세요.")

root = tk.Tk()
root.title("소수 찾기")
root.configure(bg='light yellow')
root.option_add("*Font", "Arial 10")

tk.Label(root, text="숫자를 입력하세요:", bg='light yellow', font=('Arial', 10, 'bold')).pack()

entry = tk.Entry(root, bg='light yellow')
entry.pack()

button = tk.Button(root, text="찾기", command=find_primes, bg='honeydew')
button.pack()

result_text = tk.Text(root, height=10, width=50, bg='light yellow')
result_text.pack()

root.mainloop()
        