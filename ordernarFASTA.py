from Bio import SeqIO
from functools import *

def comp(x,y):
    return len(x) - len(y)

seqs = list(SeqIO.parse('multifasta.fasta','fasta'))
#seqs.sort(cmp=lambda x,y: cmp(len(x), len(y)))
seqs.sort(key = cmp_to_key(comp))
SeqIO.write(seqs, 'multifasta_sorted.fasta','fasta')