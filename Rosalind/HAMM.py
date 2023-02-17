sample = '''GAGCCTACTAACGGGAT
            CATCGTAATGACGGCCT'''
            
def count_mutations(sample):
    sample = sample.split()
    count = 0
    for i in range(len(sample[0])):
        if sample[0][i] != sample[1][i]:
            count += 1
    return count

print(count_mutations(sample))