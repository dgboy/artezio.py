def square(nums):
    i = 0
    temp = []

    while i < len(nums):
        temp.append(nums[i] * nums[i])
        i += 1
    return temp

def even(nums):
    i = 0
    temp = []

    while i < len(nums):
        if(i % 2 == 0):
            temp.append(nums[i])
        i += 1
    return temp

def cube(nums):
    i = 0
    temp = []

    while i < len(nums):
        if(i % 2 != 0 and nums[i] % 2 == 0):
            temp.append(nums[i] * nums[i] * nums[i])
        i += 1
    return temp



temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(square(temp))
print(even(temp))
print(cube(temp))
