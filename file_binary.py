import pickle

l2d = [[5, 5, 7],
       [9, 6, 4],
       [9, 14, 4],
       [1, 4, 5]]
#print(l2d[1][2])
print(l2d)

data_file = 'data.dat'
with open(data_file, 'wb') as my_file:
    pickle.dump(l2d, my_file)
