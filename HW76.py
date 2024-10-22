# Author: Emmalyn Holmquist
# Date: 10/22/2024
# CPSC 507
# Homework 7, Problem 6

# (a) Generate a 1D NumPy array containing 10 random integers between 1 and 100.
# (b) Generate a 2D NumPy array of shape (5,5) with random floats between 0 and 1.

import numpy as np

# A - Generate a 1D NumPy array containing 10 random integers between 1 and 100.
# official numpy doc - https://numpy.org/doc/2.0/reference/random/generated/numpy.random.randint.html
# note: go up to size 101 because it will take up to but not including the upper bount
rand_array = np.random.randint(1, 101, size = 10)

#check
#print(rand_array)

# B - Generate a 2D NumPy array of shape (5,5) with random floats between 0 and 1.
random_2 = np.random.rand(5, 5)

#check
#print(random_2)