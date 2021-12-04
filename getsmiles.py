from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import RDConfig
import os
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw
import cirpy
import sys, getopt

def main(argv):
	#inputfile = ''
	#outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hqr:k:o:",[,"keyvalue=","ofile="])
	except getopt.GetoptError:
		print('getsmiles.py -type key -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-q", "--query"):
			smi = cirpy.resolve(keyvalue, 'smiles')
		elif opt in ("-r", "--resolve"):
			smi = cirpy.resolve(keyvalue, 'smiles')
		elif opt in ("-o", "--ofile"):
			outputfile = arg
			from rdkit.Chem import PyMol
			mol = Chem.MolFromSmiles(smi)
			mol_block = Chem.MolToMolBlock(mol)
			f=open(outputfile+".mol", "w")
			f.write(mol_block)
			f.close()
#print 'Input file is "', inputfile
#print 'Output file is "', outputfile
#smi = cirpy.resolve('oleuropein', 'smiles')
# print smi 
# You can get C1(=CC=NC(=N1)NC2=CC(=CC=C2C)NC(=O)C3=CC=C(C=C3)CN4CCN(CC4)C)C5=CC=CN=C5 

if __name__ == "__main__":
   main(sys.argv[1:])
#print('Number of arguments:', len(sys.argv), 'arguments.')

