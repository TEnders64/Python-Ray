
# Platform solution
"""
def checkerboard():
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4
"""
def checkerboard():
  lastCh = " "
  nextCh = "*"
  tmpCh = ""
  for i in range(0,8):
    l = ""
    for j in range(0,8):
      l += lastCh
      tmpCh = lastCh     # swap current char
      lastCh = nextCh
      nextCh = tmpCh
    print(l)
    tmpCh = lastCh     # one extra swap 
    lastCh = nextCh
    nextCh = tmpCh

checkerboard()