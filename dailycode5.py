arr = [16, 177, 4, 3, 5, 2]
def search_leaders(arr):
    n = len(arr)
    leaders = []
    
    leaders_right = arr[-1]
    leaders.append(leaders_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] > leaders_right:
            leaders_right = arr[i]
            leaders.append(arr[i])
    
    leaders.reverse()
    return leaders

print(search_leaders(arr))
