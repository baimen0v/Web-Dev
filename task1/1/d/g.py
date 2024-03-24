n = int(input())
array = input().split()
for i in range (n//2):
    array[i],array[n-i-1] = array[n-i-1], array[i]
print(" ".join(array))