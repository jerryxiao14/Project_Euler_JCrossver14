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

print(sum(sieve(2000000)))