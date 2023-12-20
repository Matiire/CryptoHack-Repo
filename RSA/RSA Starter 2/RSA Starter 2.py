num = 12
exp = 65537
p = 17
q = 23

modExp = p * q
cipher = pow(num, exp, modExp)

print(cipher)