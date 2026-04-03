num = int(input("Enter the number : "))

count = 0

if num == 0:
    print("1")
    exit(0)

while(num > 0):
    num = num // 10
    count += 1

print(f"{count}")