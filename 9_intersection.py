list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,6,9,3,11,56,79,10]
list3=[]
for value in list1:
   if value in list2:
      list3.append(value)
print(list3)