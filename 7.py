'''
what is the 10001th prime number?
'''

# number of primes <= n is approximately bounded by n/log(n)

from math import log 


def sieve(n):
    prime = [1]*(n+1) 
    p =2 
    while p*p<=n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i]=0
        p+=1 
    primes = [2]
    for i in range(3,n+1,2):
        if prime[i]:
            primes.append(i)
    return primes 
def solve(n,thresh_hyperparam = 2):
    # bianry search for bound 
    l = 0 
    r = n*n 
    upper = -1
    while l<=r:
        m = (l+r)//2 
        if m/log(m)>=thresh_hyperparam*n:
            upper = m 
            r = m-1 
        else:
            l = m+1
    return sieve(upper)[n-1]

print(solve(10001))
            
    