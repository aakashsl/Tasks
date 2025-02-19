from collections import Counter

list1=[1,5,6,9,1,5,7,1,3,5,7]

def most_occ(n):
   return Counter(n).most_common(1)

print(most_occ(list1))