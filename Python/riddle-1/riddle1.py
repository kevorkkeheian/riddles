sum = 0
mult = 0

for x in range(1, 10):
    for y in range(1, 10):
        sum = x + y
        mult = x * y
        if(sum >= 10):
            if(mult < 10):
                print(str(x) + " and " + str(y))
        break