strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def anagrams(strs):
    hashmap = {}  

    for word in strs:
        key = "".join(sorted(word))  
        if key in hashmap:
            hashmap[key].append(word)
        else:
            hashmap[key] = [word]

    return list(hashmap.values())


print(anagrams(strs))
