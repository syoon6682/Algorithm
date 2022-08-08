import numpy as np

test_array = np.array([1, 3, 5, 7], int)
print(test_array)
print(type(test_array[3]))

a = np.arange(0, 10, 2)
print(a)
print(type(a))

new = test_array + test_array
print('new: ', new)