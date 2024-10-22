# Author: Emmalyn Holmquist
# Date: 10/22/2024
# CPSC 507
# Homework 7, Problem 5

# Given two matrices:
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# (a) Calculate the eigenvalues and eigenvectors of matrix A.
# (b) Compute the inverse, determinant, and the rank of both matrices.
# (c) Multiply the two matrices element-wise and using matrix multiplication.

# A - Calculate the eigenvalues and eigenvectors of matrix A

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# official numpy doc - https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html
eigenvalues, eigenvectors = np.linalg.eig(A)

#check
#print(eigenvalues)
#print("----")
#print(eigenvectors)

# B - Compute the inverse, determinant, and the rank of both matrices.


# Inverses
# official numpy doc - https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html
inverse_A = np.linalg.inv(A)
inverse_B = np.linalg.inv(B)

#check
# print(inverse_A)
# print("----")
# print(inverse_B)

#Determinants
# official numpy doc - https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

#check
# print(det_A)
# print("----")
# print(det_B)

#Ranks
# official numpy doc - https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html
rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

#check
# print(rank_A)
# print("----")
# print(rank_B)

# C - Multiply the two matrices element-wise and using matrix multiplication.

# Element-wise:
elem_wise = A * B

# Matrix Mult:
mat_mult = np.dot(A, B)

# Check:
# print(elem_wise)
# print("----")
# print(mat_mult)