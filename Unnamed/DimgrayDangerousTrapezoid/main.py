up = "("
down = ")"

string = input()

list = list(string.strip(" "))

list_len = len(list)

counter = 0

number = 0

while counter != list_len:
  character = list[counter]
  if character == up:
    number += 1
  elif character == down:
    number -= 1
  else:
    exit("Not a bracket.")
  counter += 1
  
print(number)