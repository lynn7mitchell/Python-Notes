#at least 8 char long
#contain any sort of letters, numbers, and symbols

import re


pattern = re.compile(r'[a-zA-Z0-9$%#@]{8,}[0-9]')

password = 'asdfjasdf$8'

check = pattern.fullmatch(password)

print(check)