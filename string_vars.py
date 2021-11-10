
if __name__ == '__main__':
    s = 'abcdefghiajklam'
    print(len(s))
    print(s[1:5])
    # first 7 letters
    print(s[:7])
    # last 7 letters
    print(s[-7:])
    print(s[-7:-4])
    print(s.count('a'))
    print(s.index('a'))
    print(s.rindex('a'))

    print('----------------------------')
    s1 = 'ab\\\\c\\n\n\ndef\tghia\tjklamłóąóśćąćą'
    print(s1)


    print("I can't")
    print("Hello \"Pawel\"")
    print('Hello "Pawel"')
    print('I can\'t')