
def makeTuples(dict):
  l = []
  for k, v in dict.items():
    # print(k, v)
    l.append((k, v))
  return l

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print( makeTuples(my_dict))
