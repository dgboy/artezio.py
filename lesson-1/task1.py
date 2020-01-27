full_name = input("Enter a full name: ")

if len(full_name) > 0 and len(full_name) < 1000:
  word_list = full_name.split(' ')
  result = ''

  for word in word_list:
    result += word[0].upper() + word[1:] + ' '

  print(result)
else:
  print("The string is bad. Do something or I will not do anything!")

