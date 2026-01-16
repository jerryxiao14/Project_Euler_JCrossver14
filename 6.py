'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def solve(n):
    ans = 0
    for i in range(1,n+1): 
        ans+=i*i 
    return ((n*(n+1))//2)**2 - ans

print(solve(100))