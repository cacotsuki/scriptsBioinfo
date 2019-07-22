from collections import Counter

class dna:
    def __init__(self):
        print("Nucleotide Counter")


    def Gene(self):
        with open("/home/ivan/Documents/bioinformatics/aedes.fasta", "r") as gene:
            gene.readline()
            nucleotides_counts = Counter(char for line in gene for char in line.lower().strip())

        for (nucleotide, count) in nucleotides_counts.most_common():
            print ("Number of %s 's %d" % (nucleotide,count))

if __name__ == '__main__':
    code = dna()
    code.Gene()


