x = int(input())
for num in range(1,x+1):
    if(x/num).is_integer():
        print(num, end=" ")