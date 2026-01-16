digits = ["one","two","three","four","five","six","seven","eight","nine"]
tens = ["ten","twenty","thirty","forty","fifty",
        "sixty","seventy","eighty","ninety"]
teens = ["ten","eleven","twelve","thirteen","fourteen",
         "fifteen","sixteen","seventeen","eighteen","nineteen"]

ans = 0

for i in range(1, 1001):
    if i == 1000:
        ans += len("onethousand")
        continue

    hundreds = i // 100
    remaining = i % 100

    if hundreds > 0:
        ans += len(digits[hundreds - 1]) + len("hundred")
        if remaining != 0:
            ans += len("and")

    if remaining == 0:
        continue
    elif remaining < 10:
        ans += len(digits[remaining - 1])
    elif remaining < 20:
        ans += len(teens[remaining - 10])
    else:
        tensdigit = remaining // 10
        onesdigit = remaining % 10
        ans += len(tens[tensdigit - 1])
        if onesdigit != 0:
            ans += len(digits[onesdigit - 1])

print(ans)
