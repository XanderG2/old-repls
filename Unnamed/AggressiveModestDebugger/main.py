print("LOGIN SYSTEM")
print("Username is not case sensitive, password is")

def login():
  print()
  global username
  usr = input("username: ")
  username = usr.lower()
  password = input("password: ")
  print()
  if username == "xander":
    if password == "p@ssword":
      print(username," is logged in")
    else:
      print("Thats the wrong password.")
      exit()
  elif username == "granny":
    if password == "cappy":
      print(username," is logged in")
    else:
      print("Thats the wrong password.")
      exit()
  elif username == "zack":
    if password == "bluebouncybuddy":
      print(username," is logged in")
    else:
      print("Thats the wrong password.")
      exit()
  else:
    print(username, " is not a valid username")

login()
print()
print(username)