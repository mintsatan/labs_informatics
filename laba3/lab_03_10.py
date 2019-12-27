import collections
import re

textDict = dict(collections.Counter(re.findall(r'\w+', open('text1.txt').read().lower())))
print(textDict)
