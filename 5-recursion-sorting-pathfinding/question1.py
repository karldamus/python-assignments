# Recursion, Sorting, & Pathfinding
# Question 1: Recursive Cached Fibonacci
# 
# ©2020 Karl Damus, All Rights Reserved
#

def main():

    print(cachedfibonacci(6, cache={})) # expected output: 8
    print(cachedfibonacci(10, cache={})) # expected output: 55
    print(cachedfibonacci(100, cache={})) # expected output: 354,224,848,179,261,915,075

    ''' just for fun: comment this out to see what the 100'000th digit of the fibonacci sequence is '''
    # x = 100000
    # for i in range(x):
    #     cachedfibonacci(i, cache={})
    # print(cachedfibonacci(x, cache={}))

def cachedfibonacci(n, cache={}):
    # Base Cases
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    # Recursive Calculation
    elif n not in cache:
        cache[n] = cachedfibonacci(n-1) + cachedfibonacci(n-2)
    
    return cache[n]

if __name__ == "__main__":
    main()