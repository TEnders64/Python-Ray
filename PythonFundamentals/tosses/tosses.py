import random

heads = 0
tails = 0

for i in range (0, 5000):
  n = round(random.random())
  #print(n)
  if n == 1: heads+=1
  if n == 0: tails+=1

print ("Heads ", heads)
print ("Tails ", tails)

# Another way
print("using randint()")
heads = 0
tails = 0

for i in range (0, 5000):
  heads+=random.randint(0,1)
tails = 5000-heads
print ("Heads ", heads)
print ("Tails ", tails)
