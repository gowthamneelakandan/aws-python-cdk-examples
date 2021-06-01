list1 = ['e', 'x', 'a', 'm', 'p', 'l', 'e', 1, 4]
intList = []
strList = []
def seperateList(list1):
  for i in list1:
    if type(i) is str:
      strList.append(i)
    else:
      intList.append(i)
  print(intList)
  print(strList)
  
seperateList(list1)

def sumList(list1):
  summ = 0
  for i in list1:
    if type(i) is int:
      summ = i + summ
  print(summ)
  
sumList(list1)
