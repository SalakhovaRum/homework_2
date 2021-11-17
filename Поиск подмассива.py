def find_array(array: list, arr_find: list):
    i = 0
    j = 0
    con_array = "".join(map(str, array))
    con_arr_array = "".join(map(str, arr_find))
    while len(con_array) >= i and len(con_arr_array) > j and len(con_array) > i:
        if con_array[i + j] == con_arr_array[j]:
            j += 1
        else:
            i += 1
            j = 0
    if j == len(con_arr_array):
        return i
    else:
        return 'Поиск подмассивов не удался'