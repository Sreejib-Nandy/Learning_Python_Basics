from datetime import date

name = input(("Enter your name : "))
today = date.today()
form = f'''Dear {name}\nYou are selected!\n{today}'''
print(form)