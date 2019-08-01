from Bio.Blast import NCBIWWW
from Bio import SeqIO


#Compara as sequencias com o banco de dados NCBI

arq = SeqIO.read('/home/ivan/Documents/bioinformatics/aedes.fasta', format='fasta')
print('Buscando no banco de dados....')
result = NCBIWWW.qblast('blastn','nt', arq.seq, format_type='Text')
print(result.read())