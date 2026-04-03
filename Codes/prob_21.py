
# for i in range(0, row ):
#     print("* " * (row - i))

def pattern(n):
    if(n == 0):
        return 
    else:
        print("* " * n)
        pattern(n - 1)

row = int(input("Enter the row number : "))
pattern(row)
