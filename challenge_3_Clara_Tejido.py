"""
Shortest Superstring Problem

"""
def findOverlappingPair(str1, str2):
	"""
	Function to calculate maximum overlap in two given strings

	:param str1: first string
	:type str1: str
	:param str2: second string
	:type str2: str
	"""

	max = -1
	len1 = len(str1)
	len2 = len(str2)
	strF = ''

	# Check if suffix of str1 matches prefix of str2
	for i in range(min(len1, len2)):

		if (str1[len1-i-1:] == str2[0:i+1]):
			if (max < i):
				max = i
				strF = str1 + str2[i + 1:]

	# Check if prefix of str1 matches suffix of str2
	for i in range(min(len1, len2)):

		if (str1[0:i+1] == str2[len2-i-1:]):
			if (max < i):
				max = i
				strF = str2 + str1[i + 1:]

	return max, strF


def findShortestSuperstring(listStr):
	"""
	Function to calculate smallest string that contains each string in the given set as substring.

	:param listStr: list of DNA strings
	:type listStr: list
	"""

	while (len(listStr) != 1):
		max = -1

		# Store array index of strings involved in maximum overlap
		l = 0
		r = 0

		# Store resultant string after maximum overlap
		resStr = ''

		for i in range(len(listStr)):
			for j in range(i + 1, len(listStr)):
				res, strF = findOverlappingPair(listStr[i], listStr[j])

				# Check for maximum overlap
				if (max < res):
					max = res
					resStr = strF
					l = i
					r = j

		# Ignore last element in next cycle
		# len--;

		# If no overlap, append listStr[len] to listStr[0]
		if (max == -1):
			listStr[0] += listStr[len(listStr)-1]
			del listStr[len(listStr)-1]
		else:
			# Copy resultant string to index l
			listStr[l] = resStr

			# Copy string at last index to index r
			listStr[r] = listStr[len(listStr) - 1]
			del listStr[len(listStr) - 1]
	return listStr[0]

fasta_file = open("rosalind_fasta_shortest.py", "rt")
output_file = open("shortest.fasta", "wt")
sequences = []
current_tag = None
current_sequence = ''

for line in fasta_file:
    if line[0] == '>':
        if current_tag:
            sequences.append(current_sequence)
        current_tag = line[1:].strip()
        current_sequence = ''
    else:
        current_sequence += line.strip()

# Append the last sequence to the list
sequences.append(current_sequence)

if __name__ == "__main__":
	listStr = sequences
	shortest_superstring= findShortestSuperstring(listStr)
	output_file.write("%s" % shortest_superstring)

fasta_file.close()
output_file.close()
