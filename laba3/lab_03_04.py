'''
 Словари
'''
d1 = {
 "day": 18,
 "month": 6,
 "year": 1983
}
d2 = dict(bananas=3,apples=5,oranges=2,bag="basket")
d3 = dict([("street","Kronverksky pr."), ("house",
49)])
d4 = dict.fromkeys(["1","2"], 3)
print("Dict d1 = ", d1)
print("Dict d2 by dict()= ", d2)
print("Dict d3 by dict([])= ", d3)
print("Dict d4 by fromkeys = ", d4)
print("\n")
startDict0 = {"ready0": 3,"set0": 2, "go0": 1}
startDict1 = dict(ready1 = 3, set1 = 2, go1 = 1)
startDict2 = dict([("ready2",3), ("set2",2), ("go2",1)])
print(startDict0)
print(startDict1)
print(startDict2)
dict1 = dict.fromkeys(["key1","key2"], 77)
print(dict1)
