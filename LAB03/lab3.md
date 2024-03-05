# Part B

## Function 1

''' def factorial(number):
    if number == 0:              # 1
        return 1                 # 1
    else:
        return number * factorial(number - 1)  # 3 (1 multiplication and 2 additions) + ops done by factorial(number - 1) '''

## Function 2

''' def linear_search(lst, key, index=0):
    if index < len(lst):          # 1
        if lst[index] == key:     # 1
            return index          # 1
        else:
            return linear_search(lst, key, index + 1)
                                  # 1 (recursive call)
    else:
        return -1                 # 1  '''


# Part C

1. 
