list1=[1,2,3,4,5,6,7,8,10]

def miss(list1):
   return [i for i in range(min(list1), max(list1)+1) if i not in list1]

print(miss(list1))