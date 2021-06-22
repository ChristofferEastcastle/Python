from random import randrange


def insertionSort(array):
    for i in range(1, len(array)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


arr = [randrange(1, 100) for i in range(30)]
print(f"Original:\n{arr}\n")
insertionSort(arr)
print(f"InsertionSorted:\n{arr}")
