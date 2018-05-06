
def make_dict(list1, list2):
  new_dict = {}
  for i in range(0, len(list1)):
    new_dict[list1[i]] = list2[i]
  return new_dict


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print(make_dict(name, favorite_animal))
