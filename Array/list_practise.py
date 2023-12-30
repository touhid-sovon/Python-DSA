""" Searching in List using 'in' """

# list_1 = [1,2,3,4,5]
#
# if 5 in list_1:
#     print("Exists")
# else:
#     print("None")

'''star * operator '''

# a = [0]
# a = a*4

# print(a)

'''finding average using list methods'''
# num = []
# while True:
#     inp = (input())
#     if inp == 'done' :break
#     num.append(float(inp))
#
# average = sum(num)/len(num)
# print(average)

# list and strings

# str1 = 'sovon'
# list1 = list(str1)
#
# str2 = 'Touhidul Islam Sovon'
# list2 = list(str2.split())
#
"""split() actuablly split a string from where it found a space . We can Customize it by manually giving other arguments and 
it will spit if it find those character arguments"""
#
# str3 = 'Touhidul-Islam-Sovon'
# list3 = list(str3.split('-'))
#
# print(list3)

''' Temperature problem '''

temp = []
count = 0
n = int(input("How many day's temperature you want to measure? " ))

for i in range(1,n+1):
    t = (int(input(f"Temperature of Day {i} " )))
    temp.append(t)

average = sum(temp)/len(temp)

print(f"Average temperature is {average}")

for i in range(len(temp)):
    if temp[i] > average:
        count += 1
print(f'{count} Days are over than average temperature')
