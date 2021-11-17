#Поиск подстроки:

if __name__ == '__main__':
    text = input('Введите первую строку')
    subtext = input('Введите вторую строку')
    result = []
    stivi = False
    n = 1
    #Перебираем элементы в строках пока стиви  не будет == True
    for i, element in enumerate(text):
        if stivi:
            if n > len(subtext) - 1:
                stivi = False
                n = 1
            elif element == subtext[n]:
                n += 1
            elif element != subtext[n]:
                result = result[:-1]
                n = 1
                stivi = False
        if not stivi:
            stivi = True
            result.append(i)

    for item in result:
        print('Вхождение с ' + str(item) + ' символа',)

#Поиск подмассива:
if __name__ == '__main__':
    massive_1 = [4, 5, 1, 2, 5]
    massive_2 = [5, 1, 2, 4, 1, 4, 5, 1, 2, 5, 7, 3]
    def task(massive_1, massive_2):
        for i in range(len(massive_2)):
            if massive_1[0] == massive_2[i]:
                count = 1
                for j in range(i+1, len(massive_2)):
                    if massive_1[count] != massive_2[j]:
                        break
                    count += 1
                    if count == len(massive_1):
                        return i
    print(task(massive_1, massive_2))



#Делители:
if __name__ == '__main__':
    N = int(input('Введите число'))
    divisors = []
    #Перебераем_делители
    for i in range(N - 1, 1, -1):
        if (N % i == 0):
            divisors.append(i)
    #Добавляем 1 и само число в список
    divisors.append(N)
    divisors.append(1)
    divisors.sort(reverse=True)
    print(divisors, 'Делители')

#Сортировка пузырьком.
from random import randint

if __name__ == '__main__':
    #подбор случайных чисел
    N = 100
    a = []
    for i in range(N):
        a.append(randint(1, 99))
    print(a)
    # Наименьшие чилса двигаем влево <- | наибольшие вправо ->
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)

