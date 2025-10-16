'''
roblem Zero
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 
 is a square number because 
; it is also an odd square.

The first 5 square numbers are: 
, and the sum of the odd squares is 
.

Among the first 786 thousand square numbers, what is the sum of all the odd squares?
'''

n = 786000

def solve(n):
    return sum(i * i for i in range(1,n+1,2))

print(solve(n))