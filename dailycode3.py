arr=[1,2,2,3,4]
def dupl_arr(arr):
    if len(arr)==len(set(arr)):
        return "Duplicates not found"
    else:
        for i in arr:
            if arr.count(i)>1:
                return i
print(dupl_arr(arr))
