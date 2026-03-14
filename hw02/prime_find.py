def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("숫자를 입력하세요: "))

for i in range(2, num):
    if is_prime(i):
        print(i)
        