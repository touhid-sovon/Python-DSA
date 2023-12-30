# def first_method():
#     second_method()
#     print("This is first method")
#
# def second_method():
#     third_method()
#     print("This is second method")
#
# def third_method():
#     fourth_method()
#     print("This is third method")
#
# def fourth_method():
#     print("This is fourth method")
#
# first_method()

''' Recursive way '''
#
# def recurcive_method(n):
#     if n<1:
#         print("n is less than 1")
#     else:
#         recurcive_method(n-1)
#         print(n)
#
# recurcive_method(4)

'''Factorial Using Recursion'''

# def fact(n):
#     fact = 1
#     if n == 0 or n ==1 :
#         print(f"{fact}")
#     else:
#         for i in range(n, 1, -1):
#             fact = fact * i
#     return fact


# def fact_recursive(n):
#     assert n >= 1 and int(n) == n, 'The Number must be positive integer only'
#     if n == 0 or n == 1 :
#         return 1
#     else:
#         return n * fact_recursive(n-1)
#
#
# print(fact_recursive(-3))

''' Fibonacci series using recursion '''

# def fib(n):
#     assert n >= 1 and int(n) == n, 'Fibonacci Series has to be a Positive integer series'
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(6))

'''How to find the sum of digits of a positive integer number using recursion'''

# def sum(n):
#     assert n >= 0 and int(n) == n, f'{n} has to be a positive integer'
#     if n < 10:
#         return n
#     else:
#         rem = n % 10
#         return rem + sum(int(n/10))
#
# print(sum(10))

''' How to calculate power of a number using recursion '''

# def power(x,n):
#     assert n >= 0 and int(n) == n , 'Power has to be a positive integer'
#     if n == 0:
#         return 1
#     else:
#         power(x,n-1)
#         return  x * x
#
# print(pow(2,1))

''' Greatest Common Divisor GCD using recursion '''

# def GCD(a,b):
#     if b > a :
#         a = a+b
#         b = a-b
#         a = a -b
#
#     rem = a % b
#
#     if rem == 0:
#         return b
#     else:
#         return GCD(b,rem)
# print(GCD(12,10))


'''GCD from tutorial'''
#
# def GCD(a,b):
#     if b == 0:
#         return a
#     return GCD(b,a%b)
#
# print(GCD(48,18))

'''Decimal to Binary Conversion'''

# def D2B(n):
#     if n == 0:
#         return 0
#     else:
#         return n%2 + 10 * D2B(int(n/2))
#
# print(D2B(12))

''' Palindrome Check '''

# def palindrome(str):

''' Method 1 '''

# str = input()
#
# def palindrome(str):
#     n = len(str)
#     if n%2 ==0:
#         left = str[:n//2]
#         right = str[n//2:][::-1]
#     elif n%2 !=0:
#         left = str[:n//2]
#         right = str[n//2+1:][::-1]
#
#     print(left,right)
#     if left == right:
#         return True
#
# if palindrome(str):
#     print("Yes")
# else:
#     print("No")



'''Method 2'''

# str = input()

# def palindrome(str):
#     if len(str) < 2:
#         return True
#     elif str[0] == str[-1]:
#         print(str[1:-1])
#         # using recursion by reducing one character from each end
#         # return palindrome(str[1:-1])
#         return palindrome(str[1:len(str)-1])
#     else:
#         return False
#
# if palindrome(str):
#     print("Yes")
# else:
#     print("No")

'''Power of two '''

def powerof2(n):
    if n<1:
        return 0
    elif n == 1:
        return 1
    else:
        prev = powerof2(int(n/2))
        # print(prev)
        curr = prev * 2
        print(curr)
        return curr

powerof2(14)














