import random

def calcGrade(score):
  if score < 60: return "F"
  if score < 70: return "D"
  if score < 80: return "C"
  if score < 90: return "B"
  if score <= 100: return "A"
  return "Unknown"

for i in range (0,10):
  score = random.randint(40, 120)
  print (score, calcGrade(score))