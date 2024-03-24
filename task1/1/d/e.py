n = int(input())
array = input().split()
answer = "NO"
for i in range(1,n):
    if int(array[i]) * int(array[i-1])>0:
        answer = "YES"
        break
print(answer)