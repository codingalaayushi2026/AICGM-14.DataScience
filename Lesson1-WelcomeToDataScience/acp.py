import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 and 9
arr = np.arange(10)
print("Original Array:")
print(arr)

# 2. Replace all odd numbers with -1 without modifying the original array
new_arr = arr.copy()
new_arr[new_arr % 2 == 1] = -1

print("\nArray after replacing odd numbers with -1:")
print(new_arr)

print("\nOriginal Array remains unchanged:")
print(arr)  

# 3. Convert the original 1-dimensional array into a 2-dimensional array with two rows
arr_2d = arr.reshape(2, 5)

print("\n2-Dimensional Array:")
print(arr_2d)

# 4. Find the sum of all even numbers in the original array
even_sum = np.sum(arr[arr % 2 == 0])

print("\nSum of all even numbers:", even_sum)