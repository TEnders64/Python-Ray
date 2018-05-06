# typeList.py
import numbers

def prntListTypes(lst):
  curStr = ""
  sum = 0
  numFound = False     # Handle all zero's
  for e in lst:
    if isinstance(e, numbers.Number):
      sum += e
      numFound = True
    elif isinstance(e, str):
      curStr+= e

  if numFound and curStr:
    print("Mixed")
  elif numFound:
    print("Numeric")
  elif curStr:
    print("String")
  else:
    print("Something else")
  print("  sum: ", sum)
  print("  strings:", curStr)

prntListTypes([1, 42.3, -5])
prntListTypes(["Mary", "George", "X-men"])
prntListTypes(["A", 0])



