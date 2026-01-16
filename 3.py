'''
The prime factors of 
 13195 are  5,7,13,29
.

What is the largest prime factor of the number  600851475143
?
'''

from math import sqrt,ceil

n = 600851475143

def solve(n):

    ans = 1
    if n%2==0:
        ans = 2 
        while n%2==0:
            n//=2
    for i in range(3,ceil(sqrt(n+1)),2):
        if n%i==0:
            ans = i 
            while n%i==0:
                n//=i 
    return ans

print(solve(n))