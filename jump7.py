i = 0
while i <100:
    i = i+1
    if i%7 == 0:
        continue
    if i == 3:
        pass
    elif i%10 == 7:
        continue
    elif i//10 == 7:
        continue
    print(i)

