arr=[1,2,3,4,6,7]
n=len(arr) + 1
def find_arr(arr,n):
    total_sum = n*(n+1)//2
    arr_sum = sum(arr)
    return total_sum - arr_sum
print(find_arr(arr,n))
print("djfhvbkj")