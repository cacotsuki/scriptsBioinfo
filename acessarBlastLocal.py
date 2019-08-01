from Bio.Blast.Applications import *

#Executa blast localmente, requer blast software instalado

comando = NcbiblastnCommandline(\
     query='my.fasta', subject='my2.fasta', \
     outfmt = 0, out='saida.txt')

comando()
result = open('saida.txt','r')

linhas = result.read()
print(linhas)