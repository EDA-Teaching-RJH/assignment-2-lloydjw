### Part Four -- your code goes here. 
import random

list = []
counter = 0
for i in range(10):
    list.append(random.randint(1,100))

# for i in list[:]:
#     if i % 2 == 0:
#         list.remove(i)
#     else:
#         None

while counter < (len(list)):
    if  list[counter] % 2 == 0:
        list.pop(counter)
    else:
        counter += 1

print(list)