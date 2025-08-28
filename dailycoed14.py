from collections import defaultdict

def atMostK(s: str, k: int) -> int:
    count = defaultdict(int)
    left = 0
    res = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        res += (right - left + 1)

    return res


def substringsWithExactlyKDistinct(s: str, k: int) -> int:
    return atMostK(s, k) - atMostK(s, k - 1)


s = "pqpqs"
k = 2
print(substringsWithExactlyKDistinct(s, k))   
