a = 4

for i in range(3):
    print(i)
    print(a)
    b = 3

print('a=%s' % a)
print('b=%s' % b)

c = -1
if a > 5:
    if b > 6:
        print('a>5 and b>6')
        c = 30
else:
    c = 50
print('c=%s' % c)