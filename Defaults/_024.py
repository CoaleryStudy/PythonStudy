age = int(input())
balance = 9000

if 7 <= age <= 12:
    balance -= 650
elif age <= 18:
    balance -= 1050
else:
    balance -= 1250

print(balance)