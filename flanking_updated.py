#Flanking sequence from the BLAST hits across the genome.
#-Yashrajsinh Jadeja
#TO-DO: Fine-tune according to the pipeline.
from Bio import SeqIO
from Bio.Seq import Seq
record_index = SeqIO.index("sequence.fasta", "fasta")

accessions = []

for x in open("file.txt"):
    accessions.append(x.replace("\n",""))

#file=open("precursors.fasta","w")

flank = int(input("Enter the flank length."))

for x in accessions:
    start=int(input(f"\nEnter the S T A R T position of the hit for sequence acc {x}\n"))
    end=int(input(f"\nEnter the E N D position of the hit for sequence acc {x}\n"))
    print(f"\nMotif: {record_index[x].seq[start:end]}")
    # file.write("\n Motif\n")
    # file.write(z[x][start:end])
    print(f"\nLeft Flank: {record_index[x].seq[start-flank:start]}")
    # file.write("\n Left Flank\n")
    # file.write(z[x][start-flank:start])
    print(f"\nRight Flank: {record_index[x].seq[end:end+flank]}")
    #file.write("\n Right Flank\n")
    #file.write(z[x][end:end+flank])
#file.close()
