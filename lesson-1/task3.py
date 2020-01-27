string = input("Enter something: ")

if len(string) > 2:
  result = string[:2] + string[-2:]
  print(result)
else:
  print("Empty String")

