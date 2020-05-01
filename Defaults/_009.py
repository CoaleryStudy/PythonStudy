primes = [2, 3, 5, 7, 11]
for p in primes:
    print(p)
print("Length :", len(primes))

primes.append(13)
print(primes)

hi = primes.copy()
hi.append(17)
print(hi, primes)

list1 = [1, 2, 3]
list2 = list((4, 5, 6))

print(list1 + list2)
print(list1 * 3)

list1.extend(list2)
print(list1)

list3 = [5, 2, 4, 1, 3]
list4 = list3.copy()

list3.reverse()
print(list3)

list3.sort()
print(list3)

print(sorted(list4))
print(list4)