import json

data_file = 'data.json'
with open(data_file, 'r') as my_file:
    ll2d = json.load(my_file)
    print(ll2d)
    print(type(ll2d))
    print(type(ll2d[0][0]))