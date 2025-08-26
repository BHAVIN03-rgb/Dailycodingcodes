def isValid(s):
    stack = [] 
    mapping = {')': '(', '}': '{', ']': '['}   
    for char in s:
        if char in mapping.values():   
            stack.append(char)
        elif char in mapping:          
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()  
        else:
            return False  
    return len(stack) == 0
s = "[{()}]"
print(isValid(s))   

s2 = "[{(}]"
print(isValid(s2)) 
