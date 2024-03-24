dvoich = input()
desitich = 0
for i in range(len(dvoich)):
    num = int(dvoich[-i -1])
    desitich += num * (2**i)
print(desitich)