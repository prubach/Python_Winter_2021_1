file_path = 'test.csv'

with open(file_path, 'r') as my_file:
    lines = my_file.readlines()
    i = 1
    for line in lines:
        print(line)
        line = float(line)
        print(type(line))
        print('{}: {}'.format(i, line), end='')
        i += 1

# my_file = open(file_path, 'r')
# lines = my_file.readlines()
# i = 1
# for line in lines:
#     print('{}: {}'.format(i, line), end='')
#     i+=1
# my_file.close()
