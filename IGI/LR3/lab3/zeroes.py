def getSublist(arr: list[float]):
    '''
    return array with elements between first two zeroes
    '''
    beg = 0
    end = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            if beg != 0:
                end = i
                break
            beg = i
    return arr[beg + 1:end]
        
def max_elem(arr: list[float]):
    '''
    return max element of array
    '''
    return max(arr)

def multiply(arr: list[float]):
    '''
    return multiplication of array elements
    '''
    res = 1
    for elem in arr:
        res *= elem
    return res
