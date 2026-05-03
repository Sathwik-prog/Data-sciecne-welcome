# Import NumPy
import numpy as np

print("=== NUMPY OPERATIONS ===")

# 1. Creating Arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

print("\nArray 1:", arr1)
print("Array 2:", arr2)

# 2. Arithmetic Operations
print("\n--- Arithmetic Operations ---")
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# 3. Array Properties
print("\n--- Array Properties ---")
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)

# 4. Indexing and Slicing
print("\n--- Indexing & Slicing ---")
print("Element at index 2:", arr1[2])
print("Slice (1 to 4):", arr1[1:4])

# 5. Mathematical Functions
print("\n--- Math Functions ---")
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))

# 6. Reshaping Array
print("\n--- Reshaping ---")
arr3 = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr3.reshape(2, 3)
print("Original:", arr3)
print("Reshaped (2x3):\n", reshaped)

# 7. Special Arrays
print("\n--- Special Arrays ---")
print("Zeros:\n", np.zeros((2, 2)))
print("Ones:\n", np.ones((2, 2)))
print("Identity Matrix:\n", np.eye(3))

# 8. Random Numbers
print("\n--- Random Numbers ---")
print("Random values:", np.random.rand(3))
print("Random integer:", np.random.randint(1, 10))

print("\n=== END ===")
