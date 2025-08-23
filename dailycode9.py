strs = str(input("Enter a list of strings separated by commas: ")).split(',')

def com_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]  
            if prefix == "":
                return ""
    return prefix

print("Longest Common Prefix:", com_prefix(strs))
