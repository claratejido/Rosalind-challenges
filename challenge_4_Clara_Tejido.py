def reverse_complement(sequence):
    # create mapping of characters to their complements
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    # reverse string and replace each character with its complement
    return ''.join([complement[i] for i in sequence[::-1]])

def build_de_bruijn_graph(sequences):
    # convert the set into a list (it is easier for me to append sequences
    sequences = list(sequences)
    # do the reverse complements for each sequence and add it to a new list (rev_sequences)
    rev_sequences = sequences_rc = [reverse_complement(sequence) for sequence in sequences]
    for sequence in rev_sequences:
        sequences.append(sequence)
    # Once we have all the sequences together (normal and rc) we make sure again that there are no duplicates adding them to a new list
    sequences_no_dupl = []
    for sequence in sequences:
        if sequence not in sequences_no_dupl:
            sequences_no_dupl.append(sequence)
    graph = []
    for sequence in sequences_no_dupl: # loop over the sequences on the set
        k = len(sequence) - 1 # define k as the lenght of the sequence -1
        kmer1 = sequence[0:k] # split each sequence into a kmer 1 of all bases but the last one and a kmer 2 of all bases but the first one
        kmer2 = sequence[1:k+1]
        # add k-mers as nodes to the graph (new list)
        if (kmer1,kmer2) not in graph:
            graph.append((kmer1,kmer2))
    return graph

input_file = open("build_de_bruijn_graph.py", "rt")
output_file = open("bruijn_adjecency_list.py", "wt")

# create a set with all the sequences (lines of the fasta) -- the set will avoid that duplicated sequences are incorporated
sequences = set()
lines = input_file.readlines()

for line in lines:
    sequence = line.strip()
    sequences.add(sequence)

#make a de bruijn adjecency list for the set of sequences
bruijn_list = build_de_bruijn_graph(sequences)

# sort the list in alphabetic order
sorted_bruijn_list = sorted(bruijn_list)

# write each tuple in the sorted_bruijn_list to a new line in the output file
for tupple_seq in sorted_bruijn_list:
    output_file.write("(%s,%s)\n" % tupple_seq)

input_file.close()
output_file.close()

