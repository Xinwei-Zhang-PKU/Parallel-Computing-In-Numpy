# Given a 1-D array, judging whether it's sorted or has duplicates

import numpy as np


def is_sorted(arr):
    return not np.any(arr[1:] < arr[:-1])


def contain_duplicates(arr):
    return not np.any(arr[1:] == arr[:-1])


if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5])
    print(is_sorted(x))
    print(contain_duplicates(x))
