str1="Computer Science Engineering"
str2=str1.lower()
def first_non_repeat(str2):
   count_dict = {}
   for char in str2:
      if char in count_dict:
         count_dict[char] += 1
      else:
         count_dict[char] = 1
   return count_dict
value=first_non_repeat(str2)
print(value)

for i in value:
   if value[f'{i}']==1:
      print(i)
      break

               