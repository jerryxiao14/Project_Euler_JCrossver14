'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
-digit numbers is 9009 = 91*99
.

Find the largest palindrome made from the product of two 3
-digit numbers.
'''

def is_palindrome(digits):
    for i in range(len(digits)//2):
        if digits[i]!=digits[-1-i]:
            return False 
    return True 

max_ans = 0

for i in range(100,1000):
    for j in range(max_ans//i,1000):
        digits = []
        cur_num = i*j 
        while cur_num>0:
            digits.append(cur_num%10)
            cur_num//=10 
        if is_palindrome(digits):
            max_ans = i*j 
print(max_ans)
        