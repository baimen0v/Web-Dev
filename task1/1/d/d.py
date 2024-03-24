n = int(input())
array = input().split()
o = 0
for i in range(n):
    if(array[i]>array[i-1]):
        o+=1
print(o)