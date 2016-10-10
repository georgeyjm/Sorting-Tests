def _shuffle(array):
    from random import shuffle
    shuffle(array)
    return array

def consecutive_array(start,end,mode=1):
    '''Generates a consecutive, non-repetitive array in the given range.'''
    from random import shuffle
    try: start, end = int(start), int(end)
    except ValueError: return -1
    if mode == 1:
        return _shuffle([i for i in range(start,end)])

def random_array(start,end,count,mode=1):
    '''Generates an array containing a specific length of numbers in the given range.'''
    from random import randint
    try: start, end, count = int(start), int(end), int(count)
    except ValueError: return -1
    if mode == 1:
        return [randint(start,end-1) for i in range(count)]

def few_unique_array(start,levels,length_per_level,height_per_level,mode=1):
    '''Generates a stair-like array that has few unique values.'''
    from random import shuffle
    try: start, levels, length_per_levels, height_per_level = int(start), int(levels), int(length_per_level), int(height_per_level)
    except ValueError: return -1
    if mode == 1:
        array = []
        for i in range(start,start+levels*height_per_level,height_per_level):
            array += [i for j in range(length_per_level)]
    return _shuffle(array)

def nearly_sorted_array(start,end,count,switch_count,random=False,mode=1):
    '''Generates an array that is almost sorted.\nIf "random" is False, paramater "count" will not be used.'''
    from random import randint
    try: start, end, count, switch_count = int(start), int(end), int(count), int(switch_count)
    except ValueError: return -1
    if random: array = sorted(random_array(start,end,count))
    else: array = [i for i in range(start,end)]
    length = len(array)
    if switch_count > length // 2: return -1
    switched = []
    for i in range(switch_count):
            chosen = randint(0,length-1)
            while chosen in switched: chosen = randint(0,length-1)
            difference = randint(-(length//10),length//10) if length >= 10 else 1
            other = chosen + difference
            while other < 0 or other >= length or other == chosen or other in switched:
                difference = randint(-(length//10),length//10) if length >= 10 else 1
                other = chosen + difference
            array[chosen], array[other] = array[other], array[chosen]
    return array

def reversed_array(start,end):
    '''Generates a reversed consecutive array in the given range.'''
    try: start, end = int(start), int(end)
    except ValueError: return -1
    return list(reversed([i for i in range(start,end)]))
