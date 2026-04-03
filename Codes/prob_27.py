def generatetable(num):
    for i in range(1,11): 
       f.write(str(f"{num} x {i} = {num * i}\n"))
            


for i in range(2,21):
    with open(f"13-year-old/table_{i}.txt", "w") as f:
        generatetable(i)

    