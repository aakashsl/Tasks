list1=[1,2,3,4,4,5,6,7,8,8,9,10]

def remove_duplic(list1):
   return [x for i, x in enumerate(list1) if x not in list1[:
      i]]
print(remove_duplic(list1))