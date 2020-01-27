set1 = set(input("Enter a 1st set: ").split(' '))
set2 = set(input("Enter a 2nd set: ").split(' '))
set3 = set(input("Enter a 3rd set: ").split(' '))

print(set1)
print(set3.issubset(set1) and set3.issubset(set2))
