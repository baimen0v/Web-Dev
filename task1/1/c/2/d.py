n = int(input())
x = False
if x ==1:
   x = True
while n>1 and n%2==0:
   n /=2
   if n ==1:
      x = True
if x:
   print("YES")
else:
   print("NO")
