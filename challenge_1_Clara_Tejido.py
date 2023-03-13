
def kmer_profile(sequence, k):
    profile = {}
    array= []
    # Generate all possible k-mers of length k
    kmers = []
    for i in range(4**k):
        kmer = ''
        for j in range(k):
            index = i // (4**j) % 4
            kmer += 'ACGT'[index]
        kmers.append(kmer)
    # Initialize the count for each k-mer to 0
    for kmer in kmers:
        profile[kmer] = 0
    # Count the occurrences of each k-mer in the sequence
    for i in range(len(sequence)-k+1):
        kmer = sequence[i:i+k]
        if kmer in profile:
            profile[kmer] += 1
    # sort the dictionary with the kmers by alphabetic order
    sorted_profile = sorted(profile.items(), key=lambda x: x[0])
    # Append the values of the dictionary to a new list (array)
    for key, value in sorted_profile:
        array.append(value)
    print(profile)
    return array

sequences = ""
fasta_file = open("kmers_profile_challenge_1.fasta", "rt")
output_file = open("output_kmers.fasta", "wt")

lines = fasta_file.readlines()
for line in lines:
    if line[0] != ">":
        sequence = line.strip()
        sequences+= sequence

kmer_profile = kmer_profile(sequences,4)
for element in kmer_profile:
    output_file.write("%s " % element)

fasta_file.close()
output_file.close()