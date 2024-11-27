import sys
from enum import Enum

file = sys.argv[1]
f = open(file, 'r')

content = f.read()
content = content.split('\n')
content = [element for i, element in enumerate(content[3::]) if i%4==0]
content = ''.join(content)

min = 999
max = 0
for char in content:
    val = ord(char)
    if val > max:
        max = val
    if val < min:
        min = val

encoding = 31
if min >= 59 and max <= 104:
    print("Solexa Solexa+64")
elif min >= 33 and max <= 74:
    print("Illumina 1.8 Phred+64")
elif min >= 66 and max <= 126:
    print("Illumina 1.5 Phred+64")
elif min >= 64 and max <= 126:
    print("Illumina 1.3 Phred+64")
else:
    print("Sanger Phred+33")
    


