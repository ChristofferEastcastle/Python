from random import randint


def merge(arr1, arr2, original):
    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            original[k] = arr1[i]
            i += 1
        else:
            original[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        original[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        original[k] = arr2[j]
        j += 1
        k += 1


def mergeSort(original):
    if len(original) > 1:
        mid = len(original) // 2

        arr1 = original[:mid]
        arr2 = original[mid:]

        mergeSort(arr1)
        mergeSort(arr2)

        merge(arr1, arr2, original)


array = [randint(0, 1000) for i in range(1000)]

print(f"Original:\n{array}\n")
mergeSort(array)
print(f"Merge sorted:\n{array}")