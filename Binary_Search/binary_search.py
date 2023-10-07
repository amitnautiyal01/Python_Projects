import random
import time

def naive_search(sorted_list, target):
    """
    Naive search: Scan the entire list and check if it's equal to the target.
    If found, return the index; otherwise, return -1.
    """
    for i, num in enumerate(sorted_list):
        if num == target:
            return i
    return -1

def binary_search(sorted_list, target):
    """
    Binary search: Utilizes divide and conquer on a sorted list to find the target.
    Returns the index if found; otherwise, returns -1.
    """
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        midpoint = (low + high) // 2

        if sorted_list[midpoint] == target:
            return midpoint
        elif target < sorted_list[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1

    return -1

if __name__ == '__main__':
    # Generate a sorted list of length 10,000
    sorted_list = sorted(random.sample(range(-30000, 30001), 10000))

    # Measure execution time for naive search
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time:", (end - start), "seconds")

    # Measure execution time for binary search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time:", (end - start), "seconds")
