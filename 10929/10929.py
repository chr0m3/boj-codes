import hashlib

print(hashlib.sha224(input().encode('ascii')).hexdigest())
