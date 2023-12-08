from Crypto.PublicKey import RSA

file = open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem','r')
decrpyt = RSA.importKey(f.read())
print(file.decrypt)