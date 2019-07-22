from Bio import SeqIO

for fst in SeqIO.parse("my_seq.fasta","fasta"):
    print("%s %i" % (fst.id, len(fst)))
