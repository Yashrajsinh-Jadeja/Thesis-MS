##ID 1
##What this script does : Useful when trying to obtain flanking regions to create miRNA precursors from BLAST hits across a genome (miRNA hits with genome as reference).
##Credit the code appropriately.
##What you need : Your BLAST results along with the appropriate (start and end) query + subject coordinates of every match.
##Your reference genome in a fasta format.
##A file containing the accessions of the matches in a tabular form. (A file containing accessions, seperated by a new-line).
#You can rename the filenames in the script.

##Flanking sequence from the BLAST hits across the genome.
##Yashrajsinh Jadeja 8th Jan 2020
#TODO: Fine-tune according to the pipeline.

## Yashrajsinh-Jadeja/Thesis-MS is licensed under the
##GNU General Public License v3.0
##Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license.
##Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

from Bio import SeqIO
from Bio.Seq import Seq
record_index = SeqIO.index("sequence.fasta", "fasta") ##Indexing the reference genome.

accessions = [] ##Declaring lists.
start = []
end = []
ctr = 0

for x in open("gene.txt"):
    accessions.append(x.replace("\n","")) ##Fetching accessions from the file.

for x in open("start.txt"):
    start.append(int(x.replace("\n",""))) ##Fetching start coordinates from the file.

for x in open("end.txt"):
    end.append(int(x.replace("\n",""))) ##Fetching end coordinates from the file.

flank = int(input("Enter the flank length.")) ##Input flank length for precursors.

for x in accessions:
    # start=int(input(f"\nEnter the S T A R T position of the hit for sequence acc {x}\n")) #Enter the start coordinate.
    # end=int(input(f"\nEnter the E N D position of the hit for sequence acc {x}\n")) #Enter the end coordinate.
    print(f"\nMotif: {record_index[x].seq[start[ctr]:end[ctr]]}")
    print(f"\nLeft Flank: {record_index[x].seq[start[ctr]-flank:start[ctr]]}")
    print(f"\nRight Flank: {record_index[x].seq[end[ctr]:end[ctr]+flank]}")
    file=open(f"pni_yj_precursor_recordnum_{ctr+1}.fasta","w")
    file.write(f">pni_yj_precursor_recordnum_{ctr+1}_coord_{start[ctr]}:{end[ctr]}\n")
    file.write(str(record_index[x].seq[start[ctr]-flank:start[ctr]] + record_index[x].seq[start[ctr]:end[ctr]] + record_index[x].seq[end[ctr]:end[ctr]+flank]))
    file.close()
    ctr += 1
print("\n")
print("*" * 13)
print("All done!")
print("*" * 13)
print("\n")
print(f"The total number of precursors generated are {ctr}.")
print(f"The last precursor's gene ID was {x} and it's number was {ctr}.")
print(f"The last start coordinate was : {start[ctr-1]} and end coordinate was {end[ctr-1]}")
