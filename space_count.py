import os

my_dir = 'C:\\Temp\\t'

def sum_space(folder):
    sum = 0
    for f in os.listdir(folder):
        #type = 'd' if os.path.isdir(os.path.join(my_dir, f)) else '-'
        if os.path.isfile(os.path.join(my_dir, f)):
            size = os.path.getsize(os.path.join(my_dir, f))
            sum = sum + size
    return sum

print('Space occupied by {}: {}'.format(my_dir, sum_space(my_dir)))