from math import sqrt, ceil
x = 0
for i in range(1,100001):
    x += i
    cnt = 0
    for j in range(1,ceil(sqrt(x)+1)):
        if x%j==0:
            cnt+=1 
            if j*j!=x:
                cnt+=1 
    if cnt>=500:
        print(x)
        break 
