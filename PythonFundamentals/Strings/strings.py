first_name = "Zen"
last_name = "Coder"
print ("My name is {} {}".format(first_name, last_name))
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
# print (3*ninjas)
age = 15
if age >= 18:
  print ('Legal age')
else:
  print ('You are so young!')

# Strings and Lists assignment
words = "It's thanksgiving day. It's my birthday,too!"
idx = words.find("day")
print("Found day at", idx)
print (words.replace("day", "month"))

x = [2,54,-2,7,12,98]
print(max(x))
print(min(x))

x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0])
print(x[len(x)-1])

import math
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
list1 = x[0:math.floor(len(x)/2)] 
list2 = x[math.floor(len(x)/2):len(x)] 
list2.insert(0,list1)
print (list2)
