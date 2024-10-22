# Author: Emmalyn Holmquist
# Date: 10/22/2024
# CPSC 507
# Homework 7, Problem 2

# Given two NumPy arrays:
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([6, 7, 8, 9, 10])
# (a) Compute the sum, difference, product, and quotient of the two arrays.
# (b) Compute the dot product of the two arrays.

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

# A - Compute the sum, difference, product, and quotient of the two arrays.
sum_arrays = a + b
diff_arrays = a - b
product_arrays = a * b
quot_arrays = b/a

#check
#print(sum_arrays)
# print(diff_arrays)
# print(product_arrays)
#print(quot_arrays)

# B - dot product

dot_prod = np.dot(a, b)

#check
#print(dot_prod)