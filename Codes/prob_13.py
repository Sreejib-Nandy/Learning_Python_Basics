n = int(input("Enter the Row number : "))

for i in range (0, n):
    print("  " * (n-i), end="")
    print("* " * (2*i + 1))