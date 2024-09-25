import numpy as np

rows = int(input("Enter the number of rows: "))

cols = int(input("Enter the number of columns: "))

print("Enter the matrix elements row by row:")

arrays = []
for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    arrays.append(row)

matrix = np.array(arrays)

if rows != cols:
    print("The matrix must be square to have an Determinant.")
else:
    Determinant = np.linalg.det(matrix)
    print("Matrix:")
    print(matrix)
    print("Determinant of the matrix:")
    print(Determinant)