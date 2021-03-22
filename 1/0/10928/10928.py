import hashlib

print(hashlib.sha1(input().encode('ascii')).hexdigest())
