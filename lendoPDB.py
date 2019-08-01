#PDB = Protein Data Bank

from Bio.PDB import *

parser = PDBParser()

estrutura = parser.get_structure('BGA', '1dga.pdb')

header = parser.get_header()

print(estrutura.header['structure_method'])
print(estrutura.header['resolution'])