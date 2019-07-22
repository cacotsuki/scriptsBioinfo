from Bio.Seq import Seq

my_seq = Seq("ATG")

seq_rna = my_seq.transcribe()
print (seq_rna)


seq_dna = seq_rna.back_transcribe()
print (seq_dna)