i = 4
def multiplicationTable(i):
  for num in range(1,11):
    print(i , " x " , num , " = " , (i * num))

multiplicationTable(i)

i = [1,2,3]
def multiplicationListTable(i):
  for x in i:
    for num in range(1,11):
      print(x , " x " , num , " = " , (x * num))
      
multiplicationListTable(i)
