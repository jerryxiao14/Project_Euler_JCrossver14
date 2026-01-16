def multiply_two(a):
    carry = 0
    ans = []
    for i in range(len(a)-1,-1,-1):
        mul = (ord(a[i])-ord('0'))*2+carry 
        carry = mul//10 
        mul = mul%10 
        ans.append(chr(mul+ord('0')))
    if carry>0:
        ans.append(chr(carry+ord('0')))
    return ''.join(reversed(ans))

start = "1"
for i in range(1,1001):
    start = multiply_two(start)
    #print(f'start is now {start}')
ans = 0 
for x in start:
    ans+=int(x)
print(ans)