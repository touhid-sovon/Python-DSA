import bisect

shop_number = int(input())

shops_prices = list(map(int,input().split()))
shops_prices.sort()
n = len(shops_prices)

cons_days = int(input())
cons_days_list = []

total = 0

for i in range(cons_days):
    price = int(input())
    print(bisect.bisect(shops_prices,price))
