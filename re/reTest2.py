import re

s = 'home'

p = r'at|home'

print(re.findall(p, s))

