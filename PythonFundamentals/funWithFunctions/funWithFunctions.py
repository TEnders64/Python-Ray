
def mult(lst, n):
  l = []
  for e in lst:
    l.append(e*n)
  return l

def makeOnes(lst):
  l = []
  for e in lst:
    l2 = []
    for i in range (0, e):
      l2.append(1)
#      l2 = l.append(1)  # !!! Error
    l.append(l2)
  return l

lst = [3,5,7]
n = 5
print (makeOnes(mult(lst, n)))
