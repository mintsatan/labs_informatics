'''
 ��������� �������
'''
def sum(x, y, z=1):
 return x + y + z
print("sum(1,2,3): ",sum(1,2,3))
print("sum(1,2): ",sum(1,2))
print("sum(x=1,y=3): ",sum(x=1,y=3))
# ���������� ���������� ����������
def printArgs(*args):
 print("args of printArgs(): ",args)
 return
# ���������� ���������� ���������� � ������������������ ����
def printArgsnKwargs(m,*args,**kwargs):
 print("main argument of printArgsnKwargs(): ",m)
 print("args of printArgsnKwargs(): ",args)
 print("args of printArgsnKwargs(): ",kwargs)
 return
def checkArgs(*args, **kwargs):
  if (len(args) <= 3) and (len(kwargs) <= 3):
    print(args)
    print(kwargs)
    return
  else:
    print("��������� ���������� ������������ ����������")
printArgs("Hello World!", 1, 3, 5)
printArgsnKwargs("Earth", 7.125, radius=6371, pos=3)
print("\n")
checkArgs(5, 7, 9, e = "Earth", j = "Jupiter")