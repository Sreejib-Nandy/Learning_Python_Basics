def func_1(name="user", ending="Thank you"):
    print(f"Good Day {name}")
    print(ending)

name = input("Enter Your Name : ")
func_1()
func_1(name,"thanks")
func_1(name)
# func_1( ,"thanks")      Not happening