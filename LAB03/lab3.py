def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def linear_search(lst, key, index=0):
    if index < len(lst):
        if lst[index] == key:
            return index
        else:
            return linear_search(lst, key, index + 1)
    else:
        return -1

def binary_search(lst, key, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    
    if low <= high:
        mid = (low + high) // 2

        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            return binary_search(lst, key, mid + 1, high)
        else:
            return binary_search(lst, key, low, mid - 1)
    else:
        return -1
