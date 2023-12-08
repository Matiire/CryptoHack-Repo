def Sol(a, b):
    if b == 0:
        return a
    else:
        return Sol(b, a % b)

print(Sol(66528, 52920))