#1 задание
if __name__ == '__main__':
    import math
    summa = 0
    m = 1
    n = int(input())
    for i in range(n,n+1):
        summa += ((math.factorial(i-1)) **2)/(math.factorial(2*i))
    print(summa)

#2 задание
def print_arithmetic_progression(a, d, n):
    current_value = a

    for i in range(0, n):
        print(current_value, end=' ')
        current_value = current_value + d


a = int(input('Начальный ввод цифр '))
d = int(input('Разность '))
n = int(input('Кол-во элементов '))
print_arithmetic_progression(a, d, n)

#3 задание
from math import cos
def find(x,n):
    if n !=0:
        result = cos(x+find(x, n-1))
    else:
        result = 0
    return result
if __name__ == '__main__':
    try:
        x = int(input('Введите значение'))
        n = int(input('Введите количество'))
    except ValueError:
        print('Неверное значение')
    else:
        print(find())

#4 задание
if __name__ == '__main__':
    x = int(input())
    count = 0
    while x:
        count += x & 1
        x >>= 1
    print(count)

#5 задание
if __name__ == '__main__':
    a = []
    count = 0
    number = int(input())
    c = int(input())
    summa = 0
    while (0 < number and c < 11):
        d = number % c
        a.append(d)
        figure = number // 2
    a.reverse()
    for i in range(len(a)):
        summa += a[i]
        print(summa)
    print(a)

#6 задание
if __name__ == '__main__':
    n = int(input())
    print('*' * n)
    for i in range(n-2):
        print('*' + '' * (n-2) + '*')
    print('*' * n )















