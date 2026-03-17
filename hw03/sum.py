import tkinter as tk

def calculate_sum():
    # 반복문 방식
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    # 리스트 컴프리헨션 방식
    B = sum([i for i in range(1, 101) if i % 2 == 0])
    result_label.config(text=f"반복문 합계: {total}\n리스트 합계: {B}")

root = tk.Tk()
root.title("짝수 합 계산기")
root.configure(bg='lavender blush')
root.geometry("500x400")

title_label = tk.Label(root, text="1부터 100까지 짝수의 합 계산", bg='lavender blush', font=('Verdana', 16, 'bold'), fg='black')
title_label.pack(pady=30)

calculate_button = tk.Button(root, text="합계 계산", command=calculate_sum, bg='light pink', font=('Verdana', 14), fg='black', relief='raised', bd=5)
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="", bg='lavender blush', font=('Verdana', 12), fg='black')
result_label.pack(pady=30)

root.mainloop()