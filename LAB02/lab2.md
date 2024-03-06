## Function 1 Analysis

The provided function calculates the sum of squares of numbers up to a given number. Let's analyze its time and space complexity.

Time Complexity: O(n)

The function uses a loop that iterates from 1 to number, performing a constant amount of work for each iteration. As a result, the time complexity is linear, proportional to the value of number.

Space Complexity: O(1)

The function uses a constant amount of space regardless of the input number. The space complexity is not dependent on the size of the input.
In summary, Function 1 has a time complexity of O(n) and constant space complexity. Function 1 has a linear time complexity and constant space complexity. It efficiently calculates the sum of squares using a straightforward loop.

## Function 2 Analysis

The given function calculates the sum of the cubes of numbers up to a given number using a mathematical formula. Let's analyze its time and space complexity.

Time Complexity: O(1)

The function computes the result using a mathematical formula, which requires a constant number of arithmetic operations. The time complexity is constant, irrespective of the input number.

Space Complexity: O(1)

The function uses a constant amount of space, as it does not rely on any data structures or variables that scale with the input number.
In summary, Function 2 has constant time and space complexity. It efficiently calculates the sum of cubes using a direct formula, making it particularly efficient for large values of number.

## Function 3 Analysis

The provided function implements the Bubble Sort algorithm to sort a list. Let's analyze its time and space complexity.

Time Complexity: O(n^2)

The function contains nested loops. The outer loop runs for n-1 iterations, and the inner loop runs for n-1-i iterations, where n is the length of the list. The nested loops result in a time complexity of O(n^2) in the worst case.

Space Complexity: O(1)

The function performs in-place sorting, meaning it sorts the list without using additional memory proportional to the input size. The space complexity is constant, as it only uses a constant amount of extra space for temporary variables.
In summary, Function 3 has a time complexity of O(n^2) and constant space complexity. Bubble Sort is known for its simplicity but is less efficient than more advanced sorting algorithms for large datasets.


## Function 4 Analysis

The given function calculates the factorial of a given number using a loop. Let's analyze its time and space complexity.

Time Complexity: O(n)

The loop iterates from 1 to number, performing a constant amount of work for each iteration. The time complexity is linear, proportional to the value of number.

Space Complexity: O(1)

The function uses a constant amount of space, as it only requires variables (total and i) that do not scale with the input number.
In summary, Function 4 has a time complexity of O(n) and constant space complexity. It efficiently calculates the factorial using a straightforward loop, making it a reasonable choice for small to moderate values of number.


## Part C In-Lab Discussion:


* Name 

* Tarun Thomas


### Timing Data


| Team member | Timing for fibonacci | Timing for sum_to_number | 

|-------------|----------------------|--------------------------|

| Tarun Thomas | 7.24 | 6.28 |


## Reflection

The Fibonacci function efficiently computes Fibonacci numbers with constant space complexity. It utilizes two variables, a and b, to iteratively generate the sequence without requiring additional memory proportional to the input size. As the loop progresses, only these two variables are used, resulting in a space complexity of O(1), indicating constant space usage. Similarly, the sum_to_goal function, designed to find a pair of numbers in a list that sum to a specified goal, also maintains a constant space complexity. The loop variables i and j within the function contribute to O(1) space complexity, as they do not introduce any dependency on the input size.