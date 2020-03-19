# Print out all the prime numbers from 1 to 100. 
# Keep it simple; you should pick a language you're comfortable with.
# 1 is not a prime number
# prime number is not evenly divisible by any number that comes before it except for 1 and itself

def is_prime(n):
    if n == 1:
        return False
    if n >= 2:
        for i in range(2,n):
            if n%i == 0:
                return False
            
        return True
    
def prime_numbers(num):
    
    for n in range(num):
        if is_prime(n):
            print(n)
    
prime_numbers(100)