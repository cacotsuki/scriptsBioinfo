from Bio import SeqIO
match = 0
miss = 0
red = []
green = []


for i in SeqIO.parse('my.fasta', 'fasta'):
    ''''''
for j in SeqIO.parse('my2.fasta','fasta'):
  ''''''

print(i.seq)
print(j.seq)


for a, b in zip(i.seq,j.seq):
    if a == b:
        match +=1
    else:
        miss +=1


for i, (a, b) in enumerate(zip(i.seq, j.seq)):
    if a == b:
        green.append(i)

    if a != b:
        red.append(i)
        #print('red:',i,a,b)

print('MATCH:',match)
print('MISS:',miss)
print('-=-'*70)
print('RED:',red)
print('-='*70)
print('GREEN:',green)
