#Tricky Counter Exercise
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for num in my_list:
  counter += num

print(counter)

for item in my_list:
    continue
    print(item)

i = 0

while i <len(my_list):
    i+=1
    continue
    print(my_list[i])