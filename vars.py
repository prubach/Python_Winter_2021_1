a = 257293579275927597125972589723489578957679676813460813468234609238902578345723458234
print(type(a))
b = 10
c = a + b
print('a: {}'.format(a))
print('c: {}'.format(c))

d = 6347.635645326
d = 257293579275927597125972589723489578957679676813460813468234609238902578345723458234.0
print(type(d))
print(d)
e = 10
print(type(e))
f = d + e
print('f: {}'.format(f))

max_int = 1.792534636346346734734746e308
# limit of int
max_int = 1.8e308
print(max_int)

g = 0.0000000000000004414357593792375273
print(g)

bb = 0b101
print(bb)
xx = 0x101
print(xx)
xx = 0xf1
print(xx)

a1 = 1349
b1 = 353
c1 = a1 / b1
print('c1: ' + str(c1))
print('c1: {}'.format(c1))
c2 = int(c1)
print('c2: {}'.format(c2))

c3 = round(c1, 2)
print('c3: {}'.format(c3))
s = '45336384838549162362362366.6362'
print('-------------------')
print('s is digit: %s' % s.isdigit())
print('s is numeric: %s' % s.isnumeric())
print('s is alpha: %s' % s.isalpha())
print('s is alnum: %s' % s.isalnum())
print(s)
print('type of s: {}'.format(type(s)))
f1 = float(s)
print(type(f1))
print(f1)

print('------------------------------------')
s1 = '101'
# interpret as hexadecimal
h_s1 = int(s1, 16)
print(h_s1)
# interpret as binary
b_s1 = int(s1, 2)
print(b_s1)