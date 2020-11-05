heads = [10, 3, 0.5]

for n in range(1, 10):
    for m in range(1, 34):
        for k in range(1, 200):
            sum = 0
            sum = sum + ((heads[0] * n) + (heads[1] * m) + (heads[2] * k))
            if(sum == 100):
                if(n + m + k == 100):
                    print("10   *   " + str(n))
                    print("3    *   " + str(m))
                    print("0.5  *   " + str(k))
                    break