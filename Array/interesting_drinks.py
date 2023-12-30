shop_number = int(input())

shops_prices = list(map(int,input().split()))
shops_prices.sort()
n = len(shops_prices)

cons_days = int(input())
cons_days_list = []

def binary_search(list:list,value:int):
    low,high = 0,len(list)-1
    while (low<=high):
        mid = (low+high)//2
        if value == list[mid]:
            return mid+1
        elif value > list[mid]:
            low = mid+1
        elif value < list[mid]:
            high = mid-1
    return low

# def insert_sorted(list:list,n:int):
#     copy_list = list.copy()
#     index = binary_search(copy_list,n)
#     copy_list.insert(index, n)
#     m = copy_list.index(n)
#     if copy_list[m + 1]:
#         if copy_list[m] == copy_list[m+1]:
#             return m+1
#     return m

# list1 = [10,20,40,50,60,80,90]
#
#
# print(insert_sorted(list1,100))
# print(list1)

for i in range(cons_days):
    cons_days_list.append(int(input()))
    total = 0

    for j in range(n):
        if cons_days_list[i] < shops_prices[0]:
            break
        elif cons_days_list[i] >= shops_prices[n-1]:
            total = n
            break
        else:
            total = binary_search(shops_prices,cons_days_list[i])

    print(total)







