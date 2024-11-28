import sys
import matplotlib.pyplot as plt

# open file
file = sys.argv[1]
f = open(file, 'r')

# get contents
content = f.read()
f.close()
content = content.split('\n')
content = [element for i, element in enumerate(content[1::]) if i%4==0]

# get frequencies
frequencies = []
for sequence in content:
    acc = 0
    for c in sequence:
        if c == 'C' or c == 'G':
            acc += 1
    frequencies.append(acc/len(sequence))

# generate histogram
frequency_percentage = [frequency*100 for frequency in frequencies]
bins = range(0, 101, 1) 
plt.hist(frequency_percentage, bins=bins, edgecolor='black')
plt.title('C/G Content Distribution in Reads')
plt.xlabel('C/G Content (%)')
plt.ylabel('Number of reads')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


