for i in range(8):
    print(i)

print('-----------')
for i in range(3, 7):
    print(i)

print('-----------')
i = 100
print(i)
for i in range(8):
    if i==3:
        continue
    if i==6:
        break
    print(i)
print('i={}'.format(i))


print('-----------')
x = 10
for i in range(1, x+1):
    print(i)

print('-----------')
a = 1
while a < 17:
    print(a)
    a = a + a