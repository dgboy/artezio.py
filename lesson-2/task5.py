pwdb = [
  "qwerty",
  "123456",
  "asdfgh",
  "admin",
  "user"
]

username = input("Enter username: ")
password = input("Enter password: ")

while password not in pwdb:
  print("Password for: " + username + " is incorect\nPlease try again...")
  password = input("Enter password: ")

print("Password for: " + username + " is corect")
