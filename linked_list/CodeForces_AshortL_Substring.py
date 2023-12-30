n = int(input())

for i in range(n):
    str1 = input()
    n = len(str1)
    if n == 2:
        print(str1)
    elif n % 2 ==0:
        print(str1[::2]+str1[-1])
    else:
        print(str1[::2])
