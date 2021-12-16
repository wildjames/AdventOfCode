import hashlib

code = "ckczppom"

i = 0
while True:
    i += 1
    checkme = code + str(i)
    hashprod = hashlib.md5(checkme.encode())
    hexstring = hashprod.hexdigest()
    if hexstring.startswith("000000"):
        break

print(checkme)
