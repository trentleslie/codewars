
raw_fasta_string = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''
def fasta_to_dict(fasta_string):

    # create a dictionary to store sequence data
    sequences = {}

    for line in fasta_string.split('\n'):
        if line.startswith('>'):
            current_header = line[1:].strip()
            sequences[current_header] = ''
        else:
            sequences[current_header] += line.strip()

    return sequences

# missed the first two because I didn't mulitply by 100. derp.
def max_get_gc_content(fasta_dict):
    max_gc = 0
    for header, sequence in fasta_dict.items():
        gc_count = 0
        for nucleotide in sequence:
            if nucleotide in 'GC':
                gc_count += 1
        gc_content = gc_count / len(sequence) * 100
        if gc_content > max_gc:
            max_gc = gc_content
            max_header = header
    print(max_header, "\n", max_gc, sep = "")

max_get_gc_content(fasta_to_dict(raw_fasta_string))