str = "label"

print("crypto{", end="")
for x in str:
  print(chr(ord(x)^13), end="")
print("}")