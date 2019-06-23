#username and password terminal
#Granted or Denied based on correct password/username.

correct = True
while correct:
    name = input("Username? ")
    if name == "admin":
       pw = input("Password? ")
       if pw == "test":
          print("Entry Granted. ")
          break

