with open('words.txt', 'r') as f:
    line = f.readline()
    splitList = line.split()

    for word in splitList:
        word = word.strip('.,')
        if word.find('c') != -1:
            print(word)