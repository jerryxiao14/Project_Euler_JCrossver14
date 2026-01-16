def is_leap(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True 
            return False 
        return True 
    return False 

days = [31,28,31,30,31,30,31,31,30,31,30,31]

cur = 0
ans = 0

for i in range(1901,2001):
    leap = is_leap(i-1)
    for j in range(len(days)):
        if j==2 and leap:
            add = 29
        else:
            add = days[j]
        cur = (cur + add)%7
        if cur==6:
            ans+=1 
print(ans)
        