from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

registro = SeqRecord(Seq('ACTG'), id='biopython')
arq = open('DAZZ.fasta','w')
SeqIO.write(registro, arq, 'fasta')
arq.close()