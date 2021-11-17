for i in range(8):
    print(i)

print('-----------')
for i in range(3, 7):
    print(i)

print('-----------')
for i in range(8):
    if i==3:
        continue
    if i==6:
        break
    print(i)
