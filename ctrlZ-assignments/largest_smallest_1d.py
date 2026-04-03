index = int(input("Enter the number of index : "))

ls = []

for num in range(0, index):
    num = int(input("Enter the number: "))
    ls.append(num)

largest = ls[0]
smallest = ls[0]

for i in ls:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(f"Largest in the list : {largest}")
print(f"Smallest in the list : {smallest}")