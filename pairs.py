# Prompt: https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

# Test Case:
# Input: 1, [1, 2, 3, 4]
# Output: 3

# Input: 2, [1, 5, 3, 4, 2]
# Output: 3


def find_pairs2(k, arr): #k=target val

    arr.sort()

    i = 0
    j = 1
    pairs = 0

    while j < len(arr):

        target = arr[j] - arr[i]

        if target == k:
            pairs += 1
            j += 1
            i += 1
        elif target > k: #make smaller num bigger so the diff between bigger-smaller is smaller
            i+=1
        elif target < k: #make bigger num even bigger so diff between smaller and bigger pointer widens
            j+=1 
    return pairs

print(find_pairs2(1, [1, 2, 3, 4])) #3
print(find_pairs2(2,[1, 5, 3, 4, 2] )) #3

#Runtime: O(n log n)


def find_pairs(k, arr): #k=target val

    pairs = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]-arr[j] == k:
                pairs+=1

    return pairs

# print(find_pairs(1, [1, 2, 3, 4])) #3
# print(find_pairs(2,[1, 5, 3, 4, 2] )) #3

#Runtime: O(n^2)