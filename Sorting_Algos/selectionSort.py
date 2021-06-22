from random import randrange


def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


arr = [randrange(1, 100) for i in range(20)]
print(f"Original:\n{arr}\n")
selectionSort(arr)
print(f"SelectionSorted:\n{arr}")
