x = int(input())
c = 0
for num in range(1, x+1):
    if(x/num).is_integer():
        c+=1
print(c)