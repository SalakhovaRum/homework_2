def deliteli(number):
    number = int(input('Введите число'))
    print('Результат:',end= ' ')
    for i in range (number  - 1, 1, -1):
        if (number % i == 0):
            print(i, end=' ')

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='my first arg parser'
    )
    parser.add_argument(
        '--number',
        dest='number',
        type=int,
        help='first int value'
    )
    args = parser.parse_args()

    stivi = deliteli(args.number)
