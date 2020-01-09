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

from pyfaidx import Fasta
record_index = Fasta("sequence.fasta")
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

flank = int(input("Enter the flank length. : ")) ##Input flank length for precursors.

mot_strt = open("motif_start","w")
mot_end = open("motif_end","w")

for x in accessions:
    motif = str(record_index[x][start[ctr]-1:end[ctr]].seq)
    lflank = str(record_index[x][start[ctr]-flank-1:start[ctr]-1].seq)
    rflank = str(record_index[x][end[ctr]:end[ctr]+flank].seq)
    seq = lflank + motif + rflank
    ##motif_start = seq.find(motif) This will apply to other cases where we want to locate exact motif in the seq.
    ##MOTIF start will be flank here as we know the flank length.
    mot_strt.write(f"{str(flank)}\n")
    mot_end.write(f"{str(flank+len(motif))}\n")
    #motif_end = motif_start + len(motif)
    file=open(f"pni_yj_precursor_recordnum_{ctr+1}.fasta","w")
    file.write(f">pni_yj_precursor_recordnum_{ctr+1}_coord_{start[ctr]}:{end[ctr]}\n")
    file.write(seq)
    file.close()
    print(f"\nGENE ACC: {x}")
    print(f"ITERATION NUMBER: {ctr+1}")
    print(f"\nMotif: {motif}")
    print(f"Left Flank: {lflank}")
    print(f"Right FLank: {rflank}")
    print(f"The motif coordinate is: {flank} - {flank+len(motif)}\n")
    print(f"The length of motif is: {len(motif)}")
    #motif = len(str(record_index[x].seq[start[ctr]:end[ctr]]))
    # print(f"The motif coordinate is !!TEST!!{lflank_len} : {tot_len - rflank_len}")
    ctr += 1

mot_strt.close()
mot_end.close()

print("\n\n")
print("*" * 13)
print("All done!")
print("*" * 13)
print("\n\n")
print(f"The total number of precursors generated are {ctr}.")
print(f"The last precursor's gene ID was {x} and it's number was {ctr}.")
print(f"The last start coordinate was: {start[ctr-1]} and end coordinate was: {end[ctr-1]}")
