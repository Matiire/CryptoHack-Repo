from pwn import xor
import binascii

Str1 = binascii.unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
Str12 = binascii.unhexlify("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")

Str2 = xor(Str1,Str12)
Str23 = binascii.unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
Str3 = xor(Str2,Str23)

Flag = binascii.unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

print(xor(xor(Str2,Str3),xor(Str1,Flag)))