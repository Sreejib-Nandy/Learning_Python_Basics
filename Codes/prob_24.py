def table_1(num,index):
    if(index == 0):
        return False
    else:
        print(f"{num} x {index} = {num * index}")
        return table_1(num,index - 1)

table_1(12,10)
print("\n\n")

def table_2(num,index):
    if(index == 11):
        return False
    else:
        print(f"{num} x {index} = {num * index}")
        return table_2(num,index + 1)
    
table_2(12,1)