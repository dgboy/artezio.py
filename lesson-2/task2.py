def fun(a, b, c):
  count = 0

  for i in range(a + 1, b):
    if i % c == 0:
      count += 1
  return count



a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print("Count: " + str(fun(a, b, c)))
