import math

f = open('FileIn.txt', 'r')
data = f.read()


dictionary_size = 256
dictionary = {chr(i): i for i in range(dictionary_size)}
string = ""
compressed_data = []

for symbol in data:
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


f1 = open('FileOut.txt', 'w')
template = "%%0%dd" % math.ceil(math.log(dictionary_size, 2))

print(' '.join(map(lambda x: template % int(bin(x)[2:]), compressed_data)))
f1.write(''.join(map(lambda x: template % int(bin(x)[2:]), compressed_data)))

f1.close()
f.close()
