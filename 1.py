import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

# accessing array elements
import numpy as np

arr = np.array([1, 2, 3, 4])

print (arr[0]) 

# accessing slicing array elements
import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

#checking the data type of the array
import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

# creating arrays with a defined data type
import numpy as np

arr = np.array([1,2,3,4] , dtype='S')

print(arr)
print(arr.dtype)

#import numpy array shapes

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

print(arr.shape)

#reshaping arrays
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)

print(newarr)

# numpy joining array
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)
# searching arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

print(x)
# generate random numbers
from numpy import random

x = random.randint(100)
print(x)
