import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('Nikhil', 10, 5.8), ('Satyarth', 9, 5.6), ('Anshul', 10, 5.7)]
# Create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height:")
print(np.sort(students, order='height'))