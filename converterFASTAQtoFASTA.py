from Bio import SeqIO

SeqIO.convert('exemplo.fastq', 'fastq', 'exemplo.fasta ', 'fasta')

#FASTQ -> QUAL
SeqIO.convert('exemplo.fastq','fastq','exemploSCORE.fasta','qual')