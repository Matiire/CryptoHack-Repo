def decBigInt(bigint):
    msg = hex(bigint)
    flag = ""
    can_add = False
    to_add = "0x"
    hex_byte = []
    for x in range(2, len(msg)):
        if can_add :
            to_add += msg[x]
            hex_byte.append(to_add)
            to_add = "0x"
            can_add = False
        else:
            to_add += msg[x]
            can_add = True
                
    for y in range(0, len(hex_byte)):
        flag += chr(int(hex_byte[y], 16))
        
    return(flag)



Str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

StrI = int.from_bytes(bytearray().fromhex(Str), byteorder='big')
stringdec = decBigInt(StrI)
for x in range (256):
    flag = ""
    for c in stringdec:
        flag += chr(ord(c)^x)
    if(str(flag).find("crypto")!=-1):
        print(flag)