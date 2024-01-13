#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print('0')
    else:
        result = 0
        for i in range(c):
            result += int(sys.argv[i + 1])
        print('{}'.format(result))
