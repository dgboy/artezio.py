from collections import Counter 

dic = {'A': 100, 'B': 22, 'C': 333, 'D': 45, 'E': 50, 'F': 60}

cou = Counter(dic)
high = cou.most_common(3)

print("3 highest values:")

for i in high:
  print(i[0],": ",i[1]," ")
