def Sol(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = Sol(b % a, a)
        return gcd, y - (b // a) * x, x

print(Sol(26513, 32321))