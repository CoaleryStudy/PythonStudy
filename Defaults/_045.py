with open('words.txt', 'r') as f:
    words = f.readlines()
    for word in words:
        word = word.strip('\n')
        if word == word[::-1]:
            print(word)