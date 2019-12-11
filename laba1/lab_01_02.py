"""
 Логические операции
"""
f = True
g = False
print("f: ", f)
print("not f: ", not f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print('\n')
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print('\n\n')
'''
например:
0 <= h <= 10
Для работы с двоичными представлениями чисел предусмотрены
побитовые операции:
 x & y – побитовое И
 x | y – побитовое ИЛИ
 x ^ y – побитовое исключающее ИЛИ
 ~x – побитовая инверсия числа x
 x >> n – побитовый сдвиг числа x вправо на n бит
 x << n – побитовый сдвиг числа x влево на n бит
Для двоичного представления числового значения используется функция
bin(), при этом число передается в качестве аргумента функции,
например bin(5).
10
 Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format: %s" % (j, bin(j)))
print("k = %d; k in binary format: %s" % (k, bin(k)))
print("j & k: %d; binary: %s" % (j & k, bin(j & k)))
# побитовое AND
print("j | k: %d; binary: %s" % (j | k, bin(j | k)))
# побитовое OR
print("j ^ k: %d; binary: %s" % (j ^ k, bin(j ^ k)))
# побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k)))  # инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k >> 1, bin(k >> 1)))  # сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k << 1, bin(k << 1)))  # сдвиг на один бит влево
print("\n\n")

a = 2
b = 9
c = True
d = False
print("¬(C∧D)", not(c and d))
print("C∧D∨¬(C∧D)", (c and d) or not(c and d))
print("¬C∨D", not(c or d))
print("A<=B", a <= b)
print("A>B ∨ A==B", (a > b) or (a == b))
print("¬(A<B)", not(a < b))
print("\n\n")

s = 154
p = 6
print("s = ", s)
print("s = ", bin(s))
print("p = ", p)
print("p = ", bin(p))
print("\n\n")
s >>= 2
p >>= 2
print("s = ", s)
print("s = ", bin(s))
print("p = ", p)
print("p = ", bin(p))
