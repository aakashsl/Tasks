n=int(input())

def find_prime(n):
   if n==1 or n==2:
      return "Prime"
   for num in range(2, n+1):
      if(n%num==0 and num!=n):
         return "Not Prime"
   return "Prime"

print(find_prime(n))
   
      