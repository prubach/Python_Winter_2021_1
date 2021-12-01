import pickle

data_file = 'data.dat'
with open(data_file, 'rb') as my_file:
    ll2d = pickle.load(my_file)
    print(ll2d)
    print(type(ll2d))