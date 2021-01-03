# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def min_swaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            #move num to correct position
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            swaps+=1

    return swaps

print(min_swaps([4,3,1,2])) #3
print(min_swaps([2,3,4,1,5])) #3