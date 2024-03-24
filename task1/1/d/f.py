n = int(input())
array = input().split()
e = 0
for i in range(1,n-1):
    if int(array[i])>int(array[i-1]) and int(array[i])>int(array[i+1]):
        e += 1
print(e)