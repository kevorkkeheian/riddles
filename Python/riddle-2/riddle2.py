sum = 0
mult = 0

for x in range(1, 99):
    for y in range(1, 99):
        sum = x + y
        mult = x * y
        if(sum == mult):
            print(str(x) + " and " + str(y))