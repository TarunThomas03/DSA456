# Part B

## Function 1

```python
def factorial(number):
    if number == 0:              # 1
        return 1                 # 1
    else:
        return number * factorial(number - 1)  # 3 (1 multiplication and 2 additions) + ops done by factorial(number - 1) 
```

1. Base Case:
If number is 0, one operation is performed (checking equality).
2. Recursive Case:
In the else block, three operations are performed:
One multiplication (number * ...)
Two additions (number - 1 and the result of factorial(number - 1))
3. Time Complexity:
The time complexity is O(n), where n is the input number. Each recursive call contributes a constant number of operations.
4. Number of Operations (Recurrence Relation):
Express the number of operations as a recurrence relation:
T(n)=3+T(n−1)
T(n)=6+T(n−2)
Continue until 
T(n)=3n+T(0), where T(0) is a constant.
5. Total Number of Operations:
The sum of the arithmetic series is 3n. Each recursive call adds 3 operations.
Conclusion:
The function's time complexity is O(n).
The total number of operations for a given input n is 3n.

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

1. Base Case:
If index is less than the length of the list, one operation is performed (checking inequality).
2. Recursive Case:
If the base case is not met, the function checks for the equality of the current list element with the key.
Three operations are performed in the recursive case:
One equality check (lst[index] == key)
One recursive call (linear_search(lst, key, index + 1))
3. Time Complexity:
The time complexity is O(n), where n is the length of the list. In the worst case, the function may need to search through the entire list.
4. Number of Operations (Recurrence Relation):
Express the number of operations as a recurrence relation:
T(n) = 3 + T(n-1)
Continue until T(n) = 3n + T(0), where T(0) is a constant.
5. Total Number of Operations:
The sum of the arithmetic series is 3n. Each recursive call adds 3 operations.


# Part C

1. Writing recursive functions requires breaking down problems into manageable subproblems. The initial step involves identifying a base case, outlining conditions for terminating the recursion. Subsequently, the recursive case is defined to express the problem in smaller instances, invoking the function iteratively towards the base case. Crucially, each recursive call must bring the problem closer to resolution, preventing infinite recursion. Special cases are considered, ensuring the function's correctness across all possible inputs. Incremental testing with varying input sizes validates the function's reliability and efficiency, ensuring its effectiveness in solving complex problems.

2. Analyzing recursive functions involves looking at different aspects to ensure they work correctly and efficiently. First, we need to check if the base case, which signals when the function should stop, is clearly defined and actually stops the recursion. We must also consider the idea that if the function works on smaller parts of the problem, it should work on the entire problem. Examining time complexity helps us understand how much work the function does and how long it takes. Recursive functions might take different amounts of time compared to non-recursive ones. Space complexity involves looking at how much memory the function uses, especially the stack. Some tricks, like tail recursion optimization, can help reduce the memory used. Similar to non-recursive functions, we need to make sure recursive functions are correct, handle special cases, and are tested thoroughly. Understanding the logic behind the function is crucial, whether it's written in a recursive or non-recursive way. However, recursive functions differ in that they break down problems into smaller pieces, requiring a deeper understanding of how the function works on those smaller parts. It's important to pay attention to the unique features of recursion, like having well-defined stopping points and organized recursive calls. In summary, analyzing recursive functions involves checking if they stop when they should, considering how they handle smaller parts of a problem, understanding their time and space efficiency, and recognizing both their similarities and differences compared to non-recursive functions. This ensures that recursive solutions are both effective and reliable for solving complex problems.
