from Crypto.PublicKey import RSA
file = open("Downloads/bruce_rsa.pub", "rb")
key = RSA.importKey(file.read())
print(key.n)