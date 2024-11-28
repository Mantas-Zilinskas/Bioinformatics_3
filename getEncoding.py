import sys

# open file
file = sys.argv[1]
f = open(file, 'r')

# dump all quality evaluations into one long string
content = f.read()
f.close()
content = content.split('\n')
content = [element for i, element in enumerate(content[3::]) if i%4==0]
content = ''.join(content)

# find the lowest and highest ASCII value symbol
min = 999
max = 0
for char in content:
    val = ord(char)
    if val > max:
        max = val
    if val < min:
        min = val

# determine encoding method by checking the methods 
# from the smallest gap (max(char) - min(char)) value  
encoding = 31
if min >= 33 and max <= 74:
    print("Illumina 1.8 Phred+64")
elif min >= 59 and max <= 104:
    print("Solexa Solexa+64")
elif min >= 66 and max <= 126:
    print("Illumina 1.5 Phred+64")
elif min >= 64 and max <= 126:
    print("Illumina 1.3 Phred+64")
else:
    print("Sanger Phred+33")
    


