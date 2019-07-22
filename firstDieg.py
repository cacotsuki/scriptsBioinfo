from Bio.Seq import Seq

minha_primeira_sequencia = Seq("ATG")
print (minha_primeira_sequencia)

# sequencia complementar
seq_complement = minha_primeira_sequencia.complement()
print (seq_complement)
# sequencia reversa da complementar
seq_reverse_complement = minha_primeira_sequencia.reverse_complement()
print(seq_reverse_complement)