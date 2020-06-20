import numpy as np

# convert list into numpy array
a = np.array([0, 1, 2, 3, 4])
print(a[1])
#  The attribute size is the number of elements in the array.
print(a.size)
#  The attribute "ndim” represents the number of array dimensions or the rank of the array, in this case one.
print(a.ndim)
# The attribute "shape” is a tuple of integers indicating the size of the array in each dimension.
print(a.shape)
