import os
import rsa

os.chdir('D:\\Programmes\\Boxes\\KaliLinux\\Hackfest2020\\s3-simple-secure-system')


f = open('rsakey.der','rb')
keyDER = f.read()
f.close()

pk = rsa.PrivateKey.load_pkcs1(keyDER, format='DER')


f = open ('encrypted2.txt', 'rb')
cipher = f.read()
f.close()


pt = rsa.decrypt(cipher, pk)

print('decrypted : ', pt)