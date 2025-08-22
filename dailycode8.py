strq=str(input("Enter a String: "))
def reverse_str(strq):
    word=strq.split()
    word.reverse()
    return " ".join(word)
print("The String '"+strq + "' is reversed to")
print(reverse_str(strq))