# Sorting Test
# by George Yu

import generate, sort
from sys import exit
from time import time

algorithms = '''
[1] Some Sort (I don't know what algorithm this is called)
[2] Insertion Sort
[3] Selection Sort
[4] Bubble Sort
[5] Merge Sort
[6] Bogo Sort
\nSelect the algorithm you want to test:'''

arrays = '''
[1] Consecutive Array
[2] Random Array
[3] Few Unique Array
[4] Nearly Sorted Array
[5] Reversed Array
\nSelect the array type you want to test:'''

###### Select algorithm, array type and tries #####
algorithm = input(algorithms)
while algorithm not in (str(i+1) for i in range(6)):
    print('Invalid input!')
    algorithm = input(algorithms)
array = input(arrays)
while array not in (str(i+1) for i in range(5)):
    print('Invalid input!')
    array = input(arrays)
while True:
    try:
        tries = int(input('\nInput the number of tries:'))
        if tries <= 0: print('Tries must be bigger than 0!')
        else: break
    except ValueError:
        print('Invalid input!')
###################################################
        
################ Setting the array ################
start = input('\nInput the start value:')
if not start:
    end = 1
else:
    end = input('Input the end value:')
    if array in ('2','4'):
        count = input('Input the length of the array:')
    if array == '3':
        levels = input('Input the amount of levels:')
        level_length = input('Input the width of a level:')
        level_height = input('Input the height of a level:')
    if array == '4':
        switches = input('Input the amount of switches:')
###################################################

############## Generating the array ###############
if array == '1': unsorted_array = generate.consecutive_array(start,end)
elif array == '2': unsorted_array = generate.random_array(start,end,count)
elif array == '3': unsorted_array = generate.few_unique_array(start,levels,level_length,level_height)
elif array == '4': unsorted_array = generate.nearly_sorted_array(start,end,count,switches)
elif array == '5': unsorted_array = generate.reversed_array(start,end)
if unsorted_array == -1:
    print('\nAn error occurred while trying to generate an array!')
    print('\nTest finished!')
    exit()
###################################################

################ Sorting the array ################
print('\nSorting in progress...')
sorts, times, comparisons, accesses = [],[],[],[]
for i in range(tries):
    startTime = time()
    if algorithm == '1': sorted_array, comparison, access = sort.someSort(unsorted_array)
    elif algorithm == '2': sorted_array, comparison, access = sort.insertionSort(unsorted_array)
    elif algorithm == '3': sorted_array, comparison, access = sort.selectionSort(unsorted_array)
    elif algorithm == '4': sorted_array, comparison, access = sort.bubbleSort(unsorted_array)
    elif algorithm == '5': sorted_array, comparison, access = sort.mergeSort(unsorted_array)
    elif algorithm == '6': sorted_array, comparison, access = sort.bogoSort(unsorted_array)
    times.append(time()-startTime)
    sorts.append(sorted(unsorted_array) == sorted_array)
    comparisons.append(comparison)
    accesses.append(access)
###################################################

################ Analyze test data ################
print('Sorting finished!\n')
print('Length of array: %d'%len(unsorted_array))
print('Sorted: %d/%d (%d%%)'%(sorts.count(True),tries,sorts.count(True)/tries*100))
print('Most Comparisons: %d'%max(comparisons))
print('Least Comparisons: %d'%min(comparisons))
print('Average Comparisons: %d'%(sum(comparisons)//tries))
print('Most Array Accesses: %d'%max(accesses))
print('Least Array Accesses: %d'%min(accesses))
print('Average Array Accesses: %d'%(sum(accesses)//tries))
print('Longest Time Consumed: %.4f milliseconds'%(max(times)*1000))
print('Shortest Time Consumed: %.4f milliseconds'%(min(times)*1000))
print('Average Time Consumed: %.4f milliseconds'%(sum(times)/tries*1000))
###################################################

print('\nTest finished!')
