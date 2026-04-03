list = ['Donkey',"Cow","Dog","Cat"]

for item in list:
  with open("animals.txt") as file:
    content = file.read()
    if(item in content):
      new_content = content.replace(item, "#" * len(item))
    with open("animals.txt", "w") as file:
      file.write(new_content)

print('done')