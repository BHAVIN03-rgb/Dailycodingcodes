arr = [1, 2, -3, 3, -1, 2]

def subarr(arr):
    prefix_sum = 0
    hashmap = {}  
    result = []

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            result.append((0, i))

        if prefix_sum in hashmap:
            for prev_index in hashmap[prefix_sum]:
                result.append((prev_index + 1, i))

        if prefix_sum in hashmap:
            hashmap[prefix_sum].append(i)
        else:
            hashmap[prefix_sum] = [i]

    return result


print(subarr(arr))
