row = int(input("Enter the number of row : "))
col = int(input("Enter the number of column : "))

matrix = []

for i in range(row):
    ls = []
    for j in range(col):
        num = int(input("Enter the number: "))
        ls.append(num)
    matrix.append(ls)
    
print(matrix)

largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(row):
    for j in range(col):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print(f"Largest in the list : {largest}")
print(f"Smallest in the list : {smallest}")