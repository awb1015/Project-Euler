#Sum the even components of the fibonacci series that are below 4,000,000

total = 0

def fibonacci(x):
   return (((1 + (5**.5))**x ) - ((1 - (5**.5))**x )) / ((2**x) * (5**.5))

for i in range (0, 4000000, 3):
  #Any sufficiently large number works for the for loop
  if fibonacci(i) < 4000000:
    total = total + fibonacci(i)
  else:
    print total
    break
