import random
import time
import matplotlib.pyplot as plt

# Counters to track the number of operations
comparison_count = 0
swap_count = 0

def reset_counters():
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0

def bubble_sort(my_list):
    global comparison_count, swap_count
    reset_counters()
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparison_count += 1  # Counting comparisons
            if my_list[j] > my_list[j + 1]:
                swap_count += 1  # Counting swaps
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return comparison_count + swap_count

def selection_sort(my_list):
    global comparison_count, swap_count
    reset_counters()
    n = len(my_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparison_count += 1  # Counting comparisons
            if my_list[j] < my_list[min_index]:
                min_index = j
        swap_count += 1  # Counting swaps
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return comparison_count + swap_count

def insertion_sort(my_list):
    global comparison_count, swap_count
    reset_counters()
    n = len(my_list)
    for i in range(1, n):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key < my_list[j]:
            comparison_count += 1  # Counting comparisons
            swap_count += 1  # Counting swaps
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return comparison_count + swap_count

def quick_sort(my_list):
    global comparison_count, swap_count
    reset_counters()
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[len(my_list) // 2]
    left = [x for x in my_list if x < pivot]
    middle = [x for x in my_list if x == pivot]
    right = [x for x in my_list if x > pivot]
    comparison_count += len(my_list) - 1  # Counting comparisons
    swap_count += len(my_list)  # Counting swaps
    return comparison_count + swap_count + quick_sort(left) + quick_sort(right)

def insertion_sort_range(my_list, left, right):
    global comparison_count, swap_count
    reset_counters()
    for i in range(left + 1, right + 1):
        key = my_list[i]
        j = i - 1
        while j >= left and key < my_list[j]:
            comparison_count += 1  # Counting comparisons
            swap_count += 1  # Counting swaps
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return comparison_count + swap_count

def merge(my_list, left, middle, right):
    global comparison_count, swap_count
    reset_counters()
    left_copy = my_list[left:middle + 1]
    right_copy = my_list[middle + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_copy) and j < len(right_copy):
        comparison_count += 1  # Counting comparisons
        if left_copy[i] <= right_copy[j]:
            swap_count += 1  # Counting swaps
            my_list[k] = left_copy[i]
            i += 1
        else:
            swap_count += 1  # Counting swaps
            my_list[k] = right_copy[j]
            j += 1
        k += 1

    while i < len(left_copy):
        swap_count += 1  # Counting swaps
        my_list[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        swap_count += 1  # Counting swaps
        my_list[k] = right_copy[j]
        j += 1
        k += 1

    return comparison_count + swap_count

def merge_sort(my_list, left, right):
    global comparison_count, swap_count
    reset_counters()
    if left < right:
        middle = (left + right) // 2
        merge_sort(my_list, left, middle)
        merge_sort(my_list, middle + 1, right)
        merge(my_list, left, middle, right)

def main():
    list_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]

    # Dictionary to store T(n) values for each algorithm
    tn_values = {
        'Bubble Sort': [],
        'Selection Sort': [],
        'Insertion Sort': [],
        'Quick Sort': [],
        'Insertion Sort with Range': [],
        'Merge Sort': []
    }

    # Dictionary to store execution times for each algorithm
    execution_times = {
        'Bubble Sort': [],
        'Selection Sort': [],
        'Insertion Sort': [],
        'Quick Sort': [],
        'Insertion Sort with Range': [],
        'Merge Sort': []
    }

    for size in list_sizes:
        # Generate worst-case scenario (reverse sorted list)
        worst_case_list = list(range(size, 0, -1))

        # Bubble Sort
        reset_counters()
        tn_values['Bubble Sort'].append(bubble_sort(worst_case_list))
        start_time = time.time()
        bubble_sort(worst_case_list)
        end_time = time.time()
        execution_times['Bubble Sort'].append(end_time - start_time)

        # Selection Sort
        reset_counters()
        tn_values['Selection Sort'].append(selection_sort(worst_case_list))
        start_time = time.time()
        selection_sort(worst_case_list)
        end_time = time.time()
        execution_times['Selection Sort'].append(end_time - start_time)

        # Insertion Sort
        reset_counters()
        tn_values['Insertion Sort'].append(insertion_sort(worst_case_list))
        start_time = time.time()
        insertion_sort(worst_case_list)
        end_time = time.time()
        execution_times['Insertion Sort'].append(end_time - start_time)

        # Quick Sort
        reset_counters()
        tn_values['Quick Sort'].append(quick_sort(worst_case_list))
        start_time = time.time()
        quick_sort(worst_case_list)
        end_time = time.time()
        execution_times['Quick Sort'].append(end_time - start_time)

        # Insertion Sort with Range
        reset_counters()
        tn_values['Insertion Sort with Range'].append(insertion_sort_range(worst_case_list, 0, len(worst_case_list) - 1))
        start_time = time.time()
        insertion_sort_range(worst_case_list, 0, len(worst_case_list) - 1)
        end_time = time.time()
        execution_times['Insertion Sort with Range'].append(end_time - start_time)

        # Merge Sort
        reset_counters()
        merge_sort(worst_case_list, 0, len(worst_case_list) - 1)
        tn_values['Merge Sort'].append(comparison_count + swap_count)
        start_time = time.time()
        merge_sort(worst_case_list, 0, len(worst_case_list) - 1)
        end_time = time.time()
        execution_times['Merge Sort'].append(end_time - start_time)

    # Plotting T(n) vs. n
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    for algorithm, values in tn_values.items():
        plt.plot(list_sizes, values, label=algorithm)
    plt.title('T(n) vs. n')
    plt.xlabel('List Size (n)')
    plt.ylabel('T(n)')
    plt.legend()

    # Plotting execution time vs. n
    plt.subplot(1, 2, 2)
    for algorithm, times in execution_times.items():
        plt.plot(list_sizes, times, label=algorithm)
    plt.title('Execution Time vs. n')
    plt.xlabel('List Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
