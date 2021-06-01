list1 = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
list2 = []
def sortAscList(list1,list2):
  while list1:
    min = list1[0]
    for x in list1:
      if x < min:
        min = x
    list2.append(min)
    list1.remove(min)
  print(list2)
  print(''.join(list2))
    
sortAscList(list1,list2)

list3 = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
list4 = []
def sortDscList(list3,list4):
  while list3:
    max = list3[0]
    for x in list3:
      if x > max:
        max = x
    list4.append(max)
    list3.remove(max)
  print(list4)
  print(''.join(list4))
    
sortDscList(list3,list4)
