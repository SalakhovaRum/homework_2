n = int(input())
a = []
for i in range(n): #кол-во строк
    row = input().split()
    last_element = int(row[-1])
    new_element = 0
    for j in range(len(row)): #индекс элемента в строке
        new_element = row[j]
        row[j] = int(row[j])+int(last_element)
        last_element = new_element
        a.append(row)
    print(a)