
def fndCharInStr (lst, ch):
  l = []
  for s in lst:
    print(s)
    if not isinstance(s, str):
      # print("Not a string")
      continue                  # Ignore numbers
    if s.find(ch) >= 0:
#    if ch in s:      # Both ways work
#      l+=s           # Problem
      l.append(s)

  return l

l = fndCharInStr(["A", 42, " MAYDAY"], "A")
print(l)


