def sum(num):
    if(num == 1):
        return num
    else:
        return num + sum(num - 1)
    
num = int(input("Enter a number : "))
print(f"The num of {num} natural number is : {sum(num)}")