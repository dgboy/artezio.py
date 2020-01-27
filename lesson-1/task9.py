num_list = [1, 3, 5, 6, 3, 5, 6, 1, 10, 11, 10]

res = []
for i in num_list:
  if i not in res:
    res.append(i)

print(res)
