# names.py

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
"""
for e in users.items():
  #print(e)
  for i in range (0, len(e)):
    print(i, e[i])
    print("")
"""
for e in users.items():
  # Print out names in each role
  # e[0] is the role, e[1] the list
  print(e[0] + ":")
  for i in range(0, len(e[1])):
    # General way
    #print(" ", e[1][i])
    n = e[1][i]["first_name"] + " " + e[1][i]["last_name"]
    print(" ", i, "-", n, "-", len(n)-1)
