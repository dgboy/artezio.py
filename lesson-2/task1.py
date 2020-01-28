x = int(input("Enter a length: "))
count = 0

for i in range(0, x + 1):
  if i % 2 != 0:
    print(str(i) + ': ' + str(i * i))
    count += 1

print("Count: " + str(count))
