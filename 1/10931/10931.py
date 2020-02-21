import hashlib

print(hashlib.sha384(input().encode('ascii')).hexdigest())
