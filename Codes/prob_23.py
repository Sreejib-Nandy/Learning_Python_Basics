def list_update(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Sreejib","joyjit","arindam","aritra","arnab","Writoriddho","sayoni","anwesha"]

print(f"The new list is : {list_update(l,"ar")}")