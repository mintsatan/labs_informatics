hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
bin = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
s = input()
result = ''
negativeFlag = False
if s >= '7f':
    print("that's not my work :)")
    exit(0)
if s[0] == '-':
    negativeFlag = True
    s = s[1:]
result = ''.join(map(lambda x: bin[hex.index(x)], s))
if negativeFlag:
    result = ''.join(map(lambda x: '0' if int(x) else '1', result))
    print(result)
    result = str(int('1' + result) + 1)
    result = result[1:]
    k = 0
    if result[-1] == '2':
        for i in range(len(result) - 2, 1, -1):
            if result[i] == '1':
                k += 1
            else:
                break
        result = result[:len(result) - k - 2] + '1' + '0' * (k + 1)
print(result)
