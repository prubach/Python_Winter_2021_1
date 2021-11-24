l1 = [4232, 245326, 57467347, 362363, 36364, 346123782]

print(l1[0])
print(l1[5])
print(l1[-1])

l2 = l1[1:5]
print(l2)
l2.append(68979)
print(l2)
l2.insert(2, 966743)
l2[1] = 5723
print(l2)

l3 = l2
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)

print('--------------')
print('')

l4 = [3636, 78785, 1526, 255.453, 'Hello Python 3', 75675]
print(l4)

# Extract the word 'Python' from l4
print(l4[4][6:12])
print(l4[4].split(' ')[1])


# Sum all number values of l4
l5 = l4[0:4] + l4[5:]
print(sum(l5))

my_sum = 0
for el in l4:
    if type(el)==int or type(el)==float:
        my_sum = my_sum + el
print(my_sum)
l6 = [el for el in l4 if type(el)==int or type(el)==float]

sum_l6 = sum([el for el in l4 if type(el)==int or type(el)==float])
print(l6)
print(sum_l6)


l1 = [4232, 245326, 57467347, 362363, 36364, 346123782]
l1i = [el*2 for el in l1]
print(l1i)

l1ii = []
for el in l1:
    l1ii.append(el*2)
print(l1ii)
