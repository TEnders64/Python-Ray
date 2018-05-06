dog = ("Canis Familiaris", "dog", "carnivore", 12)
print (dog[2])
for data in dog:
  print (data)
dog = dog + ("domestic",) # comma makes it a string
print (dog)
dog = dog[:3]  + ("man's best friend",) + dog[4:]
print (dog)
