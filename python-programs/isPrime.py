i = 4
def isPrime(i):
  if i > 1:
    for num in range(2,i):
      if (i % num) == 0:
        print("Not Prime")
        break
    else:
      print("Prime")
      
isPrime(i)  
