# Author: Emmalyn Holmquist
# Date: 10/22/2024
# CPSC 507
# Homework 7, Problem 4

# Create a NumPy array of angles:
# angles = np.array([0, 30, 45, 60, 90])
# (a) Convert the angles from degrees to radians.
# (b) Calculate the sine, cosine, and tangent of the angles.

# A - Convert the angles from degrees to radians.

import numpy as np
import math
angles = np.array([0, 30, 45, 60, 90])

# There is probably a numpy func for this but I chose the long way. Mult each angle by pi/180
radians = (math.pi/180) * angles

#check
#print(radians)

# B - Calculate the sine, cosine, and tangent of the angles.

# I guessed the np func for these!
sine = np.sin(angles)
cosine= np.cos(angles)
tangent = np.tan(angles)

#check
#print(sine)
#print(cosine)
#print(tangent)