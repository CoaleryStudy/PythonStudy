price_list = list(map(int, input().split(';')))
for price in reversed(sorted(price_list)):
    print('{0:>9,}'.format(price))