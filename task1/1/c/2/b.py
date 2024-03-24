n = int(input())
num=2
while num <=n:
    if(n/num).is_integer():
        print(num)
        break
    else:
        num+=1 