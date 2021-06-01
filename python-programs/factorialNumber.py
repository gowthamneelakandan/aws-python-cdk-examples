i = 4
def factorialNumber(i):
  fact = 1
  if i < 0:
    print("No factorial for {}".format(i))
  elif i == 0:
    print("factorial is 1")
  else:
    for num in range(1,i+1):
      fact = fact * num
      print(fact)
      
factorialNumber(i) 
