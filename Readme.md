# Explanations

### getEncoding.py
Prints the most likely quality encoding method for provided FASTQ sequence.
supported methods:
- Sanger Phred+33
- Solexa Solexa+64
- Illumina 1.3+ Phred+64
- Illumina 1.5+ Phred+64
- Illumina 1.8+ Phred+33

### GCFrequency
Creates a frequency histogram, showing how many reads were found with certain G/C frequencies

# Instructions

### getEncoding.py
Launch in terminal with the FASTQ file as an argument
example:
>>> getEncoding.py [file_name.fastq]

### GCFrequency
Launch in terminal with the FASTQ file as an argument
example:
>>> GCFrequency [file_name.fastq]