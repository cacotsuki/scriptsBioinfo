from Bio.Seq import Seq

my_seq = Seq("ATG")

#transcricao
seq_rna = my_seq.transcribe()
seq_dna = seq_rna.back_transcribe()

#traducao
seq_proteina = seq_rna.translate()
seq_proteina_dna = seq_dna.translate()

print(seq_proteina_dna)

