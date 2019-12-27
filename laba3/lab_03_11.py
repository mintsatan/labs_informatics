import heapq
import collections


class Node(collections.namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(collections.namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huff_encode(s):
    h = []
    for a, freq in collections.Counter(s).items():
        h.append((freq, len(h), Leaf(a)))

    heapq.heapify(h)

    c = len(h)
    while len(h) > 1:
        freq1, c1, left = heapq.heappop(h)
        freq2, c2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, c, Node(left, right)))
        c += 1

    code = {}
    if h:
        [(freq0, c0, root)] = h
        root.walk(code, "")
    return code


f = open('FileIn.txt', 'r')
s = f.read()
code = huff_encode(s)
encode = ''.join(code[a] for a in s)
print(len(code), len(encode))
for i in sorted(code):
    print("{}: {}".format(i, code[i]))

f1 = open('FileOut.txt', 'w')
f1.write(encode)

f.close()
f1.close()
