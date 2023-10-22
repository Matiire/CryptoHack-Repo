import base64
given = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
given_bytes = bytes.fromhex(given)
ans = base64.b64encode(given_bytes).decode()
print(ans)