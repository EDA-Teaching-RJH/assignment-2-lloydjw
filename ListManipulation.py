### Part Three -- your code goes here. 
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list.sort()
extra =[7,8]

for i in list:
    if 1 in list:
        list.remove(1)
    else:
        break

list.extend(extra)

print(list)
