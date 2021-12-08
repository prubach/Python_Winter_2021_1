import os

print(__file__)

my_file_path = __file__

my_parent_dir = os.path.dirname(my_file_path)
my_file_name = os.path.basename(my_file_path)
print(my_parent_dir)
print(my_file_name)

#in_path = os.path.join(os.getcwd(), 'data', '.keep')

in_path = os.path.join(os.getcwd(), 'data', '.keep')

print(in_path)

my_dir = 'c:\\Users\\prubac'
#print(os.listdir('c:\\Users'))
for f in os.listdir(my_dir):
    type = 'd' if os.path.isdir(os.path.join(my_dir, f)) else '-'
    size = os.path.getsize(os.path.join(my_dir, f))
    print('{} {} {}'.format(type, size, f))

