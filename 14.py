maxsteps = 0
maxnum = 0

for i in range(1,1000001):
    n = i 
    steps = 0 
    while n!=1:
        if n%2:
            n = 3*n+1 
        else:
            n = n//2 
        steps+=1 
    if steps>maxsteps:
        maxsteps = steps 
        maxnum = i 
print(maxnum)
    