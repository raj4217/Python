import pickle

data = [1,2,3,4,5,6]

pickle.dump(data, open('data.pickle','wb'))

print(pickle.load(open('data.pickle','rb')))
