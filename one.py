'''
If we list all the natural numbers below 
 that are multiples of 
 or 
, we get 
 and 
. The sum of these multiples is 
.

Find the sum of all the multiples of 
 or 
 below 
.
'''

ans = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        ans += i
print(ans)
