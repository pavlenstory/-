def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)#5*4*3*2*1

print(fact(5))