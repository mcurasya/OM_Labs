import math
def func(x):
  return (7-math.cos(x/5))/3

x=0
for i in range(100):
  x=func(x)
  print(x)