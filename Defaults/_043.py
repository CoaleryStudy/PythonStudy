import pickle

name = 'Coalery'
age = 19
address = "부산"
scores = {'korean' : 90, 'english' : 85, 'mathematics' : 100, 'science' : 95}

with open('{}.studentinfo'.format(name), 'wb') as f:
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(scores, f)

with open('{}.studentinfo'.format(name), "rb") as f:
    pName = pickle.load(f)
    pAge = pickle.load(f)
    pAddress = pickle.load(f)
    pScores = pickle.load(f)

    print(pName)
    print(pAge)
    print(pAddress)
    print(pScores)