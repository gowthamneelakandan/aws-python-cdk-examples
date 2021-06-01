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

lower = 3
upper = 29
def isPrimeLimit(lower,upper):
  for num in range(lower,upper + 1):
    if num > 1:
      for i in range(2,num):
        if (num % i) == 0:
          break
        else:
          print(num)
          
isPrimeLimit(lower,upper)
