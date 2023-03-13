
# open input and output files, give the kmer lenght a value of 3 and create a new empty dictionary (sequences)
k=3
sequences = {}
current_tag = None
current_sequence = ''
fasta_file = open("rosalind_fasta.py", "rt")
output_file = open("adjecency_list.fasta", "wt")

# put all the sequences in the input file in the empty dictionary, so each tag is the key and the sequence is the value
for line in fasta_file:
    if line[0] == '>':
        if current_tag:
            sequences[current_tag] = current_sequence
        current_tag = line[1:].strip()
        current_sequence = ''
    else:
        current_sequence += line.strip()
sequences[current_tag] = current_sequence

# Iterate over the keys and values of the dictionary
for key1, value1 in sequences.items():
    #for each of the sequences we are gonna compare it with the rest of the sequences in the dictionary
    for key2, value2 in sequences.items():
    # True when: the tag is diferent (we are not comparing the same sequence) AND the three last nucleotides of the sequence are the same as the three first of the sequence we are comparing with
        if key1 != key2 and value1[len(value1)-k:len(value1)] == value2[:k]:
    # In this case we indicate the tags of the two sequences as overlapping ones in the output adjency list
            output_file.write("%s %s\n" % (key1, key2))

fasta_file.close()
output_file.close()

