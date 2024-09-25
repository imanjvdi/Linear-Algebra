import numpy as np

# Getting the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the matrix elements row by row:")

# Taking the matrix elements from the user
arrays = []
for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    arrays.append(row)

# Converting the list to a numpy array
matrix = np.array(arrays)

# Checking if the matrix is invertible
if rows != cols:
    print("The matrix must be square to have an inverse.")
elif np.linalg.det(matrix) == 0:
    print("The matrix is singular and does not have an inverse.")
else:
    invers = np.linalg.inv(matrix)
    print("Matrix:")
    print(matrix)
    print("Inverse of the matrix:")
    print(invers)



