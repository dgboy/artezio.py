def fac(n):
  if n > 1:
    return n * fac(n - 1)
  else:
    return 1



n = int(input("Enter n: "))

print(str(n) + "! = " + str(fac(n)))
