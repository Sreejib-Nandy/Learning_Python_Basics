with open("poems.txt") as f:
    word = f.read()
    if('twinkle' in word or "Twinkle" in word):
     print("The word 'twinkle' is present in the text")
    else :
     print("The word 'twinkle' is not present in the text")

print("Finish!")
