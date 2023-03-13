
def get_circular_seq(circular_seq, sequences, k):
#loop over the list of sequences until the end of the dictionary
    while sequences:
        # check if all but the first nucleotide of the sequence 1 is equal to all but the last nucleotide for each of the other sequences in the dictionary (sequence 2)
        for key in sequences:
            if (circular_seq[len(circular_seq)-k:] == sequences[key][:k]):
            # if True: append the last nucleotide of the sequence 2 to the circular string and remove the sequence 1 from the dictionary
                circular_seq += sequences[key][-1:]
                del sequences[key]
                break
    # I realise that the first sequence in the circular string was being repeated at the end, so I remove the last 49 nucelotides to make the shortest circular string
    if circular_seq[:k] == circular_seq[len(circular_seq)-k:]:
        circular_seq = circular_seq[:len(circular_seq)-k]
    return circular_seq

# Open input and output files
input_file = open("kmers_challenge_5.py", "rt")
output_file = open("output_challenge_5.txt", "wt")

# create an empty dictionary to store all the sequences (lines with 50 bp sequences) from the input file
sequences = {}
lines = input_file.readlines()
i = 1
for line in lines:
    sequences[i] = line.strip()
    i += 1

# define a k_size variable which will be 49 bp (one less than the lenght of the sequences)
k = len(sequences[1]) - 1

# start the circular_seq
circular_seq = sequences[1]
# delete the first sequence from the list of sequences (as it has been already included in the circular seq)
del sequences[1]

#write an output file that will contains the circular minimal lenght sequence that contains all the
output_file.write(get_circular_seq(circular_seq, sequences, k))
