sequences = []
current_tag = None
current_sequence = ''

fasta_file = open("N50N75.fasta.py", "rt")
output_file = open("N50_output.fasta", "wt")

# create a list with all the sequences (lines of the fasta)
lines = fasta_file.readlines()
for line in lines:
    sequence = line.strip()
    sequences.append(sequence)

# First order the sequences
sorted_sequences = sorted(sequences, key=lambda s: len(s))

# I first count the total bases of the dataset, then I look count the number of bases to arrive to the 50% and 75% of that lenght
total_letters = 0
letters= 0

for sequence in sorted_sequences:
    total_letters+= len(sequence)

### N50 and N75 ####
for sequence in sorted_sequences:
    for letter in sequence:
        letters+=1
        if total_letters%2==0 and letters==total_letters/2 or total_letters%2 !=0 and letters==(total_letters+1)/2:
            n50 = len(sequence)
            output_file.write("%s %s" % (n50,n75))
        if total_letters%2==0 and letters==total_letters/4 or total_letters%2 !=0 and letters==(total_letters+1)/4:
            n75 = len(sequence)

fasta_file.close()
output_file.close()