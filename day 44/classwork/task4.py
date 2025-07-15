"https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python"
# Complementary DNA
def DNA_strand(dna):
    result = ''
    for nucleotide in dna:
        if nucleotide == 'A':
            result += 'T'
        elif nucleotide == 'T':
            result += 'A'
        elif nucleotide == 'C':
            result += 'G'
        elif nucleotide == 'G':
            result += 'C'
    return result