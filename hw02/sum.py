#반복문 + 조건문
total = 0 
for i in range(1,101):
    if i % 2 == 0:
        total += i
print(total)

#지능형 리스트
B = sum([ i for i in range(1,101) if i % 2 == 0])
print(B)