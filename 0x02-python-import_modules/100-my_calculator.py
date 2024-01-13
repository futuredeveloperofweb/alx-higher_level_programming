#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    c = len(sys.argv)

    if c != 4:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)

    m = int(sys.argv[1])
    x = sys.argv[2]
    n = int(sys.argv[3])

    if x == '+':
        print('{} {} {} = {}'.format(m, x, n, add(m, n)))
    elif x == '-':
        print('{} {} {} = {}'.format(m, x, n, sub(m, n)))
    elif x == '*':
        print('{} {} {} = {}'.format(m, x, n, mul(m, n)))
    elif x == '/':
        print('{} {} {} = {}'.format(m, x, n, div(m, n)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
