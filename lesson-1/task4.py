string = input("Enter something: ")
word_list = string.split(' ')
counter = 0

for word in word_list:
  if len(word) >= 2 and word[0] == word[-1]:
    counter += 1

print(counter)
