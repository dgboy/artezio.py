def myrange(start, end, step = 1):
  num_list = []
  i = start

  if start < end:
    while i < end:
      num_list.append(i)
      i += step
  else:
    while i > end:
      num_list.append(i)
      i += step

  return num_list


print(myrange(1, 50, 5))
print(myrange(10, 5, -2))
print(myrange(100, 0, -10))
