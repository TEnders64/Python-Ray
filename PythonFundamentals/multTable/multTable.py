

def prntTable():
  print("x    1   2   3   4   5   6   7   8   9  10  11  12") 
  for r in range(1, 13):
    rStr = ""
    for c in range (1, 13):
      sNum = str(r*c)
      rStr+= sNum.rjust(4, " ")
    print(str(r).ljust(2," "), rStr)

prntTable()

