x = int(input("Enter the value of x : "))
n = int(input("Enter the value of n : "))

y = 1       
count = 0  

while count < n:
    y = y * x
    count += 1

print(f"y = {y}")