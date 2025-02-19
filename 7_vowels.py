str1="Welcome to Velalar College"

def count_vowels(srt1):
   vowels = "aeiouAEIOU"
   count=0
   temp=""
   for char in srt1:
      if char not in temp:
         if char in vowels:
            temp+=char
            count+=1
   return count

print(count_vowels(str1))

   