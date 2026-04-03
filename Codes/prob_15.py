num = int(input("Enter the row number : "))

if(num > 2):
    for i in range(1, num  + 1):
        if(i == 1 or i == num):
            print("* " * num)
        if(i > 1 and i< num):
            print("* ", end ="")
            print("  " * (num - 2), end ="")
            print("* ")
else:
    print("Enter the row number greater than 2")