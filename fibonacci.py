# Prompt:Compute nth fibonacci number

def fibonacci(num):
    '''Recursion solution w/o memoizaton. Runtime O(2^n)'''

    if num == 0:
        return 0

    if num == 1:
        return 1

    return fibonacci(num-1) + fibonacci(num-2)


# print(fibonacci(5))

def fibonacci_faster(num, memo={}): #memo will be an empty dict
    '''Recursion solution WITH memoizaton. Runtime O(n)'''

    # print('memo:', memo)
    if num == 0 or num == 1:
        return num

    if not num in memo:
        memo[num] = fibonacci_faster(num-1, memo)+fibonacci_faster(num-2, memo)

    return memo[num]


# fibonacci_faster(5)

def fibonacci_bottom_up(num):
    '''Bottom-up solution. Runtime O(n)'''

    if num == 0 or num == 1:
        return num

    memo = {}
    
    memo[0] = 0
    memo[1] = 1


    for n in range(2, num+1):
        memo[n] = memo[n-1]+ memo[n-2]
        print('memo:', memo)

    return memo[n-1]+memo[n-2]

fibonacci_bottom_up(5)

# memo: {0: 0, 1: 1, 2: 1}
# memo: {0: 0, 1: 1, 2: 1, 3: 2}
# memo: {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}
# memo: {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5}







