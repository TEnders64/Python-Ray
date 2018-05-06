import numbers

def drawStars(lst):
  for e in lst:
    if isinstance(e, numbers.Number) :
      print("*"*e)
    elif isinstance(e, str) :
      print(e[0]*len(e))

drawStars([2, 5, "Aaardvark"])
in = 42



