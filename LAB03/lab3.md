# Part B

## Function 1

```python
def factorial(number):
    if number == 0:              # 1
        return 1                 # 1
    else:
        return number * factorial(number - 1)  # 3 (1 multiplication and 2 additions) + ops done by factorial(number - 1) 
```

## Function 2

```python
def linear_search(lst, key, index=0):
    if index < len(lst):          # 1
        if lst[index] == key:     # 1
            return index          # 1
        else:
            return linear_search(lst, key, index + 1)
                                  # 1 (recursive call)
    else:
        return -1                 # 1  
```

# Part C

1. Writing recursive functions requires breaking down problems into manageable subproblems. The initial step involves identifying a base case, outlining conditions for terminating the recursion. Subsequently, the recursive case is defined to express the problem in smaller instances, invoking the function iteratively towards the base case. Crucially, each recursive call must bring the problem closer to resolution, preventing infinite recursion. Special cases are considered, ensuring the function's correctness across all possible inputs. Incremental testing with varying input sizes validates the function's reliability and efficiency, ensuring its effectiveness in solving complex problems.

2. Analyzing recursive functions involves looking at different aspects to ensure they work correctly and efficiently. First, we need to check if the base case, which signals when the function should stop, is clearly defined and actually stops the recursion. We must also consider the idea that if the function works on smaller parts of the problem, it should work on the entire problem. Examining time complexity helps us understand how much work the function does and how long it takes. Recursive functions might take different amounts of time compared to non-recursive ones. Space complexity involves looking at how much memory the function uses, especially the stack. Some tricks, like tail recursion optimization, can help reduce the memory used. Similar to non-recursive functions, we need to make sure recursive functions are correct, handle special cases, and are tested thoroughly. Understanding the logic behind the function is crucial, whether it's written in a recursive or non-recursive way. However, recursive functions differ in that they break down problems into smaller pieces, requiring a deeper understanding of how the function works on those smaller parts. It's important to pay attention to the unique features of recursion, like having well-defined stopping points and organized recursive calls. In summary, analyzing recursive functions involves checking if they stop when they should, considering how they handle smaller parts of a problem, understanding their time and space efficiency, and recognizing both their similarities and differences compared to non-recursive functions. This ensures that recursive solutions are both effective and reliable for solving complex problems.
