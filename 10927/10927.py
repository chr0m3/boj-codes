import hashlib

print(hashlib.md5(input().encode('ascii')).hexdigest())
