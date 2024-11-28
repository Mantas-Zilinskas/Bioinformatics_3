import sys
import math

# open file
file = sys.argv[1]
f = open(file, 'r')

# get contents
content = f.read()
f.close()

# split into reads
lines = content.split('\n')
reads = ['\n'.join(lines[i:i+4]) for i in range(0, len(lines), 4)]

# split reads into lines
reads_lines : list[list[str]] = [read.split('\n') for read in reads] 
del reads_lines[-1]

# add G/C frequency percentage
for read_lines in reads_lines:
    acc = 0
    for char in read_lines[1]:
        if char == 'C' or char == 'G':
            acc += 1
    read_lines.append(acc/len(read_lines[1]))

# create buckets
buckets = {}
bucket_size = 5
for i in range(0, 101, bucket_size):
    buckets[i] = 0

# sort frequencies into buckets
for read_lines in reads_lines:
    value = math.trunc(read_lines[4]*100 - (read_lines[4]*100 % bucket_size))
    buckets[value] += 1

# find peak buckets
peak_buckets = []
last = 0
current = 0
next = 0 
current_key = 0
for key in buckets:
    last = current
    current = next
    next = buckets[key]
    if current > last and current > next:
        peak_buckets.append(current_key)
    current_key = key

# create mini buckets
mini_buckets = {}
for i in range(0, 101):
    mini_buckets[i] = 0

# sort frequencies into mini buckets
for read_lines in reads_lines:
    value = math.trunc(read_lines[4]*100)
    mini_buckets[value] += 1

# find largest mini bucket inside 
# inside each peak bucket
largest_mini_bucket_keys = []
for peak_bucket_key in peak_buckets:
    largest_mini_bucket_key = 0
    largest_mini_bucket_size = 0
    for i in range(bucket_size):
        if mini_buckets[peak_bucket_key + i] > largest_mini_bucket_size:
            largest_mini_bucket_size = mini_buckets[peak_bucket_key + i]
            largest_mini_bucket_key = peak_bucket_key + i
    largest_mini_bucket_keys.append(largest_mini_bucket_key)

# log to file first five reads 
# from largest mini buckets 
rf = open("peak_frequency_reads.txt", "w")
for bucket in largest_mini_bucket_keys:
    acc = 0
    text = f"\n\nsequences from bucket {bucket}:\n\n"
    for read_lines in reads_lines:
        if math.trunc(read_lines[4] * 100) == bucket:
            acc += 1
            text += "\n".join(read_lines[:-1:])
            text += "\n"
            if acc == 5:
                break
    rf.write(text)    
    




# after reflecting:
# I could have just calculated mini buckets
# right from the start and used their sums 
# instead regular buckets