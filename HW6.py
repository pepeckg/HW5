def selection_sort(any_list):
    n = len(any_list)
    sorted_list = list(any_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    return sorted_list

def binary_search(A, VAL): # A - это список где ищем, VAL - что ищем
    N = len(A)
    result_ok = False
    first = 0
    last = N - 1

    while first <= last:
        middle = (first + last) // 2
        if VAL == A[middle]:
            first = middle
            last = first
            result_ok = True
            POS = middle
            break
        else:
            if VAL > A[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if result_ok == True:
        print(f'элемент {VAL} найден под индексом {POS}')
    else:
        print(f'элемент {VAL} не найден')

unsorted_list = [38, 35, 44, 34, 43, 37, 33, 41, 31, 45, 46, 47, 42, 50, 30]
print('неотсортированный список:', unsorted_list)

sorted_list = selection_sort(unsorted_list)
print('отсортированный список: ', sorted_list)

target_element = 33
binary_search(sorted_list, target_element)
