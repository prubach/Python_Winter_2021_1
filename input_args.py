import sys

if __name__ == '__main__':
    print(sys.argv)
    for arg in sys.argv:
        print(arg)
        print(type(arg))

    #print(sys.argv[1])
    #print(type(sys.argv[1]))
