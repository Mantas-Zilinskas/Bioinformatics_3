# Explanations

### getEncoding.py
Prints the most likely quality encoding method for provided FASTQ sequence.
supported methods:
- Sanger Phred+33
- Solexa Solexa+64
- Illumina 1.3+ Phred+64
- Illumina 1.5+ Phred+64
- Illumina 1.8+ Phred+33

### GCFrequency.py
Creates a frequency histogram, showing how many reads were found with certain G/C frequencies

### getGCFrequencyPeakValues.py
Outputs up to five reads for each peak of G/C freaquencies into a file named 'peak_freaquency_reads.txt'

First finds the peaks using 5% frequency intervals, then takes those peak intervals and finds 1% interval inside each peak with the most reads and finally gets first five values from each one of those 1% intervals

# Instructions

### getEncoding.py
Launch in terminal with the FASTQ file as an argument
example:
>>> getEncoding.py [file_name.fastq]

### GCFrequency.py
Launch in terminal with the FASTQ file as an argument
example:
>>> GCFrequency.py [file_name.fastq]

### getGCFrequencyPeakValues.py
Launch in terminal with the FASTQ file as an argument
example:
>>> getGCFrequencyPeakValues.py [file_name.fastq]
