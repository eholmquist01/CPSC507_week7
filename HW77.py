# Author: Emmalyn Holmquist
# Date: 10/22/2024
# CPSC 507
# Homework 7, Problem 7

# Given a NumPy array of shape (6,):
# arr = np.array([1, 2, 3, 4, 5, 6])
# (a) Convert the 1D array into a 2D array of shape (2,3).
# (b) Extract the first row and the second column from the reshaped array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])

# A - Convert the 1D array into a 2D array of shape (2,3).
reshaped_array = arr.reshape(2, 3)

#check
#print(reshaped_array)

# B - Extract the first row and the second column from the reshaped array.

extraction_row = reshaped_array[0]
extraction_col = reshaped_array[:, 1]
#check
# print(extraction_row)
# print("----")
# print(extraction_col)