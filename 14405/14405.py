import re

if re.fullmatch(re.compile('^(pi|ka|chu)*$'), str(input())) is not None:
    print('YES')
else:
    print('NO')
