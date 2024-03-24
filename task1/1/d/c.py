n = int(input())
array = input().split()
o = 0
for i in range(n):
    if int(array[i]) > 0:
        o +=1
print(o)