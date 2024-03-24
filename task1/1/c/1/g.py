x = int(input())
for num in range(2,x+1):
    if(x/num).is_integer():
        print(num)
        break