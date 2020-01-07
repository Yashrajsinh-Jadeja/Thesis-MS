#ID
#What this script does : Useful when trying to obtain flanking regions to create miRNA precursors from BLAST hits across a genome (miRNA hits with genome as reference).

#What you need : Your BLAST results along with the appropriate (start and end) query + subject coordinates of every match.
#Your reference genome in a fasta format.
#A file containing the accessions of the matches in a tabular form. (A file containing accessions, seperated by a new-line).
#You can rename the filenames in the script.

#Flanking sequence from the BLAST hits across the genome.
#Yashrajsinh Jadeja
#TODO: Fine-tune according to the pipeline.

from Bio import SeqIO
from Bio.Seq import Seq
record_index = SeqIO.index("sequence.fasta", "fasta") #Indexing the reference genome.

accessions = []

for x in open("file"):
    accessions.append(x.replace("\n","")) #Fetching accessions from the file.

#file=open("precursors.fasta","w") #TODO writing a fasta.

flank = int(input("Enter the flank length.")) #Input flank length for precursors.

for x in accessions:
    start=int(input(f"\nEnter the S T A R T position of the hit for sequence acc {x}\n")) #Enter the start coordinate.
    end=int(input(f"\nEnter the E N D position of the hit for sequence acc {x}\n")) #Enter the end coordinate.
    print(f"\nMotif: {record_index[x].seq[start:end]}")
    print(f"\nLeft Flank: {record_index[x].seq[start-flank:start]}")
    print(f"\nRight Flank: {record_index[x].seq[end:end+flank]}")

#file.close()
