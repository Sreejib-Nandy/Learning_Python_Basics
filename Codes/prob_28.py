with open("text.txt") as file:
    content = file.read()
    if("Donkey" in content):
        new_content = content.replace("Donkey","######")
with open("text.txt", "w") as file:
    file.write(str(new_content))