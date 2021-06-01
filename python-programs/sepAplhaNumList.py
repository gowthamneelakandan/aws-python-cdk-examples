qwe = ['e', 'x', 'a', 'm', 'p', 'l', 'e', 1, 4]
intList = []
strList = []
def seperateList(qwe):
  for i in qwe:
    if type(i) is str:
      strList.append(i)
    else:
      intList.append(i)
  print(intList)
  print(strList)
  
seperateList(qwe)
