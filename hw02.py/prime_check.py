def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    return True
num = int(input("숫자를 입력하세요."))

if is_prime(num):
    print(f"{num} 소수입니다.")
else:
    print(f"{num} 소수가 아닙니다.")