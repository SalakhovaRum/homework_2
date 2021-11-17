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
