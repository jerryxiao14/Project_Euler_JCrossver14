grid = []
for _ in range(100):
    grid.append(input())


def addStrings(num1: str, num2: str) -> str:
    carry = 0
    oneind = len(num1) - 1
    twoind = len(num2) - 1
    ans = []

    while oneind >= 0 and twoind >= 0:
        add = (ord(num1[oneind]) - ord('0')) + (ord(num2[twoind]) - ord('0')) + carry
        carry = 1 if add >= 10 else 0
        add %= 10
        ans.append(chr(add + ord('0')))
        oneind -= 1
        twoind -= 1

    while oneind >= 0:
        add = (ord(num1[oneind]) - ord('0')) + carry
        carry = 1 if add >= 10 else 0
        add %= 10
        ans.append(chr(add + ord('0')))
        oneind -= 1

    while twoind >= 0:
        add = (ord(num2[twoind]) - ord('0')) + carry
        carry = 1 if add >= 10 else 0
        add %= 10
        ans.append(chr(add + ord('0')))
        twoind -= 1

    if carry == 1:
        ans.append('1')

    return ''.join(reversed(ans))

start = grid[0]
for i in range(1,len(grid)):
    start = addStrings(start,grid[i])
print(start)
