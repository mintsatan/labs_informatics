import itertools

s = input()
for i in range(len(s)):
    print(' '.join(map(''.join, itertools.combinations(s, i + 1))))
