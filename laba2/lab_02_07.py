x = list(input())
x.reverse()
x = list(map(lambda x: '10' if x == 'a' else '11' if x == 'b' else x, x))
x = sum(map(lambda e: int(e) * 12 ** x.index(e), x))
s = ''
while x > 0:
    el = x % 14
    s += str(el) if el < 10 else ['a', 'b', 'c', 'd'][el % 10]
    x //= 14
print(s[::-1])
