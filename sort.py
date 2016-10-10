def someSort(array):
    '''Time Complexity: O(n^2)'''
    length = len(array)
    comparisons, accesses = 0,0
    for i in range(length):
        for j in range(i+1,length):
            comparisons += 1
            if array[i] > array[j]:
                accesses += 1
                array[i], array[j] = array[j], array[i]
    return array, comparisons, accesses

def insertionSort(array):
    '''Time Complexity: O(n^2)'''
    length = len(array)
    comparisons, accesses = 0,0
    for i in range(length):
        for j in range(i):
            comparisons += 1
            if array[j] > array[i]:
                accesses += 1
                array.insert(j,array[i])
                del array[i+1]
    return array, comparisons, accesses

def selectionSort(array):
    '''Time Complexity: O(n^2)'''
    length = len(array)
    comparisons, accesses = 0,0
    for i in range(length-1):
        min = i
        for j in range(i+1,length):
            comparisons += 1
            if array[j] < array[min]:
                accesses += 1
                min = j
        array[i], array[min] = array[min], array[i]
    return array, comparisons, accesses

def bubbleSort(array):
    '''Time Complexity: O(n^2)'''
    length = len(array)
    comparisons, accesses = 0,0
    for i in range(length-1):
        for j in range(length-1,i,-1):
            comparisons += 1
            if array[j] < array[j-1]:
                accesses += 1
                array[j], array[j-1] = array[j-1], array[j]
    return array, comparisons, accesses

def mergeSort(array,comparisons=0,accesses=0):
    '''Or is it quick sort??'''
    if len(array) == 1: return array, comparisons, accesses
    result = []
    middle = len(array) // 2
    left, comparisons, accesses = mergeSort(array[:middle],comparisons,accesses)
    right, comparisons, accesses = mergeSort(array[middle:],comparisons,accesses)
    leftIndex, rightIndex = 0,0
    while leftIndex < len(left) and rightIndex < len(right):
        comparisons += 1
        if left[leftIndex] > right[rightIndex]:
            result.append(right[rightIndex])
            rightIndex += 1
        else:
            result.append(left[leftIndex])
            leftIndex += 1
    result += left[leftIndex:] + right[rightIndex:]
    return result, comparisons, accesses

def bogoSort(array):
    '''Time Complexity: O(1) (best), O(∞) (worst)'''
    from random import shuffle
    comparisons, accesses = 0,0
    while True:
        for i in range(1, len(array)):
            comparisons += 1
            if array[i] < array[i-1]: break
        else:
            break
        shuffle(array)
        accesses += 1
    return array, comparisons, accesses
