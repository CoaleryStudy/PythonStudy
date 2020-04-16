files = input().split()

print(list(map(lambda s: "{0:03d}.{1}".format(int(s.split('.')[0]), s.split('.')[1]), files)))

# Have to use Lambda Expression
# Very Dirty