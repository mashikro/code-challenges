# Prompt: Child is running up a staircase with n steps and can hop either 1, 2 or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs

#we do this or this because child can hop either 1, 2, or 3 steps, so you add recursive calls rather than multiply.

def calculate_possibility(n, memo={}): # n - number of steps, an arr
    print('memo:', memo)
    
    if n == 1 or n == 2 or n == 3:
        return n

    if not n in memo:
        memo[n] = calculate_possibility(n-1, memo)+calculate_possibility(n-2, memo)+calculate_possibility(n-3, memo)

    return memo[n]

print(calculate_possibility(5))