n = int(input())
array = input().split()
for i in range(n):
    array[i]=int(array[i])
    if array[i] % 2 == 0:
        print(array[i], end=" ")
