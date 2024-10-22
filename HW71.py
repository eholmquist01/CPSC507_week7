# Author: Emmalyn Holmquist
# Date: 10/22/2024
# CPSC 507
# Homework 7, Problem 1

# Given a NumPy array of integers:
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# (a) Reverse the array.
# (b) Extract all odd numbers from the array.
# (c) Replace all odd numbers in the array with -1 without changing the original array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# A - Reverse the array.

# official numpy doc - https://numpy.org/devdocs/reference/generated/numpy.flip.html
reversed_arr = np.flip(arr)

# check
# print(reversed_arr)

# B - Extract all odd numbers from the array.

odd_arr = arr[arr % 2 == 1]

#check
#print(odd_arr)

# C - Replace all odd numbers in the array with -1 without changing the original array.

# official numpy doc - https://numpy.org/devdocs/reference/generated/numpy.copy.html
new_arr = np.copy(arr)
new_arr[new_arr % 2 ==1] = -1

#check
#print(new_arr)