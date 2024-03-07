import random
import time
import matplotlib.pyplot as plt

# Step 1

def bubble_sort(my_list):
    steps = 0
    n = len(my_list)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps += 4  # 4 operations, 3 for the swap and one for the comparison
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return steps

def selection_sort(my_list):
    steps = 0
    n = len(my_list)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            steps += 3  # 3 operations for comparison
            if my_list[j] < my_list[min_index]:
                min_index = j

        steps += 3  # 3 operations for swap
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    return steps

def insertion_sort(my_list):
    steps = 0
    n = len(my_list)

    for i in range(1, n):
        key = my_list[i]
        j = i - 1

        while j >= 0 and key < my_list[j]:
            steps += 4  # 4 operations, 3 for shifting and one for the comparison
            my_list[j + 1] = my_list[j]
            j -= 1

        steps += 1  # 1 operation for the final placement
        my_list[j + 1] = key

    return steps

def quick_sort(my_list):
    steps = 0

    def partition(arr, low, high):
        nonlocal steps
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            steps += 3  # 3 operations for comparison
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        steps += 3  # 3 operations for swap
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        nonlocal steps
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(my_list, 0, len(my_list) - 1)
    return steps

# Step 2

def calculate_tn(sort_function, my_list):
    sorted_list = my_list.copy()
    t_n = sort_function(sorted_list)
    return t_n

# Step 3

list_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]

for size in list_sizes:
    rand_list = [random.randint(0, 101) for _ in range(size)]
    rand_list.sort(reverse=True)

    tn_bubble = calculate_tn(bubble_sort, rand_list)
    tn_selection = calculate_tn(selection_sort, rand_list)
    tn_insertion = calculate_tn(insertion_sort, rand_list)
    tn_quick = calculate_tn(quick_sort, rand_list)

    print(f"List Size: {size}")
    print(f"Bubble Sort T(n): {tn_bubble}")
    print(f"Selection Sort T(n): {tn_selection}")
    print(f"Insertion Sort T(n): {tn_insertion}")
    print(f"Quick Sort T(n): {tn_quick}")
    print()

# Step 4

def measure_time(sort_function, my_list):
    start_time = time.time()
    sort_function(my_list)
    end_time = time.time()
    return end_time - start_time

bubble_times = []
selection_times = []
insertion_times = []
quick_times = []

for size in list_sizes:
    rand_list = [random.randint(0, 101) for _ in range(size)]
    rand_list.sort(reverse=True)

    bubble_time = measure_time(bubble_sort, rand_list.copy())
    selection_time = measure_time(selection_sort, rand_list.copy())
    insertion_time = measure_time(insertion_sort, rand_list.copy())
    quick_time = measure_time(quick_sort, rand_list.copy())

    bubble_times.append(bubble_time)
    selection_times.append(selection_time)
    insertion_times.append(insertion_time)
    quick_times.append(quick_time)

# Plotting T(n) vs n

plt.figure(figsize=(10, 6))
plt.plot(list_sizes, bubble_times, label='Bubble Sort')
plt.plot(list_sizes, selection_times, label='Selection Sort')
plt.plot(list_sizes, insertion_times, label='Insertion Sort')
plt.plot(list_sizes, quick_times, label='Quick Sort')
plt.title('Algorithm Completion Time vs List Size')
plt.xlabel('List Size (n)')
plt.ylabel('Algorithm Completion Time (seconds)')
plt.legend()
plt.show()
