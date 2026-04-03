num = int(input("Enter a number : "))

count = 0
for i in range (2,num):
    if(num%i == 0):
        count += 1
        break
        

if(count == 0):
     print(f"{num} is a PRIME NUMBER")
else:
     print(f"{num} is not a PRIME NUMBER")