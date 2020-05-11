import collections
import heapq
import math


class Encoder:
    def encode(self, s):
        return str

    def decode(self, s):
        return str


class HuffmanEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 1

    def __setCompressionCoef(self, newCoef):
        self.compressionCoef = newCoef

    def getCompressionCoef(self):
        return self.compressionCoef

    def encode(self, s):
        length = len(s)

        class Node(collections.namedtuple("Node", ["left", "right"])):
            def walk(self, code, acc):
                self.left.walk(code, acc + "0")
                self.right.walk(code, acc + "1")

        class Leaf(collections.namedtuple("Leaf", ["char"])):
            def walk(self, code, acc):
                code[self.char] = acc or '0'

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

        result = ''.join(code[a] for a in s)
        self.__setCompressionCoef(len(result) / length)
        return result

    def decode(self, s):
        return str


class LZEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 1

    def __setCompressionCoef(self, newCoef):
        self.compressionCoef = newCoef

    def getCompressionCoef(self):
        return self.compressionCoef

    def encode(self, s):
        length = len(s)
        dictionary_size = 256
        dictionary = {chr(i): i for i in range(dictionary_size)}
        string = ""
        compressed_data = []

        for symbol in s:
            string_plus_symbol = string + symbol
            if string_plus_symbol in dictionary:
                string = string_plus_symbol
            else:
                compressed_data.append(dictionary[string])
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
                string = symbol

        if string in dictionary:
            compressed_data.append(dictionary[string])

        template = "%%0%dd" % math.ceil(math.log(dictionary_size, 2))

        result = ''.join(map(lambda x: template % int(bin(x)[2:]), compressed_data))
        self.__setCompressionCoef(len(result) / length)
        return result

    def decode(self, s):
        return str


inputString = "Python is a widely used high-level programming language for general-purpose programming, created by " \
              "Guido van Rossum and first released in 1991. "

huffEncoder = HuffmanEncoder()
print(huffEncoder.encode(inputString))
print(huffEncoder.getCompressionCoef())

lzEncoder = LZEncoder()
print(lzEncoder.encode(inputString))
print(lzEncoder.getCompressionCoef())
