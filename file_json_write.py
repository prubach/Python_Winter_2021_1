import json

l2d = [[5, 5, 7],
       [9, 6, 4],
       [9, 14, 4],
       [1, 4, 5],
       ['ab', "bf", 'yey']]
#print(l2d[1][2])
print(l2d)

data_file = 'data.json'
with open(data_file, 'w') as my_file:
    json.dump(l2d, my_file)