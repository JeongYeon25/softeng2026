def c2f(c):
    return c * 9/5 + 32
def f2c(f):
    return (f-32) * 5/9
choice = input("℃인지 ℉인지 선택하세요")
temp = float(input("온도를 입력하세요"))

if choice == "℃":
    print(f"{c2f(temp)}℉")
elif choice == "℉":
    print(f"{f2c(temp)}℃")
else: 
    print("다시 입력하세요.")