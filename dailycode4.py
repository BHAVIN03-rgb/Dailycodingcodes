import math
arr1=[1,3,4,7]
arr2=[2,5,6,8]
def arr_swap(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    
    space = m + n
    space = math.ceil(space / 2)
    
    while space > 0:
        i = 0
        j = space
        
        while j < m + n:
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]
            
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]
            
            i += 1
            j += 1
        
        if space == 1:
            spacespace = 0
        else:
            gap = math.ceil(gap / 2)

arr_swap(arr1, arr2)

print("arr1 =", arr1)
print("arr2 =", arr2)
