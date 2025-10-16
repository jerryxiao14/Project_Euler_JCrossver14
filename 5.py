'''
2520 is the smallest number that can be divided by each of the numbers from 
 to 
 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 
1 to 20
?
'''

def gcd(a,b):
    if a%b==0:
        return b 
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

x = 2520
for i in range(11,21):
    x = lcm(x,i)
print(x)

