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

def err():
    print("\nOops something's not right.")
    print("Try checking the files that you have provided.")
    print("\nLinux sometimes has conflicts with '.txt' files so you can try renaming your files to just 'gene', 'start' and 'end' and edit this script by searching for 'gene.txt' and changing file names accordingly." )
    print("\nCheck if there are COLUMN NAMES left over in your files. THERE SHOULD BE NO COLUMN NAMES, JUST THE VALUES. It's a common 'copy-paste' error. Open each of the 3 files and check the first and last lines if they have any unwanted entries left.")
    print("\nIf this still didn't work, create an issue request on 'www.github.com/Yashrajsinh-Jadeja/' or just contact me via Twitter '@omnomgenome' or email: 'yashrajjadeja97@gmail.com' ")
    return

def welcome():
    print("          _____                    _____                    _____                    _____                    _____                    _____            _____          ")
    print("         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \          /\    \         ")
    print("        /::\____\                /::\    \                /::\    \                /::\    \                /::\    \                /::\____\        /::\    \        ")
    print("       /::::|   |                \:::\    \              /::::\    \              /::::\    \              /::::\    \              /:::/    /       /::::\    \       ")
    print("      /:::::|   |                 \:::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /:::/    /       /::::::\    \      ")
    print("     /::::::|   |                  \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /       /:::/\:::\    \     ")
    print("    /:::/|::|   |                   \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \        /:::/    /       /:::/__\:::\    \    ")
    print("   /:::/ |::|   |                   /::::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \      /:::/    /       /::::\   \:::\    \   ")
    print("  /:::/  |::|___|______    ____    /::::::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \    /:::/    /       /::::::\   \:::\    \  ")
    print(" /:::/   |::::::::\    \  /\   \  /:::/\:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/    /       /:::/\:::\   \:::\    \ ")
    print("/:::/    |:::::::::\____\/::\   \/:::/  \:::\____\/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/____/       /:::/__\:::\   \:::\____\ ",end="")
    print("\::/    / ~~~~~/:::/    /\:::\  /:::/    \::/    /\::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\:::\    \      \::/    /\:::\    \       \:::\   \:::\   \::/    / ",end="")
    print(" \/____/      /:::/    /  \:::\/:::/    / \/____/  \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \:::\    \      \/____/  \:::\    \       \:::\   \:::\   \/____/ ")
    print("             /:::/    /    \::::::/    /                 |:::::::::/    /            \::::::/    /    \:::\    \               \:::\    \       \:::\   \:::\    \     ")
    print("            /:::/    /      \::::/____/                  |::|\::::/    /              \::::/    /      \:::\    \               \:::\    \       \:::\   \:::\____\    ")
    print("           /:::/    /        \:::\    \                  |::| \::/____/               /:::/    /        \:::\    \               \:::\    \       \:::\   \::/    /    ")
    print("          /:::/    /          \:::\    \                 |::|  ~|                    /:::/    /          \:::\    \               \:::\    \       \:::\   \/____/     ")
    print("         /:::/    /            \:::\    \                |::|   |                   /:::/    /            \:::\    \               \:::\    \       \:::\    \         ")
    print("        /:::/    /              \:::\____\               \::|   |                  /:::/    /              \:::\____\               \:::\____\       \:::\____\        ")
    print("        \::/    /                \::/    /                \:|   |                  \::/    /                \::/    /                \::/    /        \::/    /        ")
    print("         \/____/                  \/____/                  \|___|                   \/____/                  \/____/                  \/____/          \/____/         ")
    print("\n\nAUTHOR: Yashrajsinh Jadeja ")
    print("\nGitHub: github.com/Yashrajsinh-Jadeja/")
    print("\nEmail: yashrajjadeja97@gmail.com")
    print("\nYashrajsinh-Jadeja/Thesis-MS is licensed under the GNU General Public License v3.0. ")
    print("Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license.")
    print("Copyright and license notices must be preserved.")
    print("Contributors provide an express grant of patent rights.")
    print("\n(c) miRacle flanking_updated_v3")
    print("\nThis program will generate precursors '.fasta' sequences accordingly as per the chosen flank length.")
    print("\nThe '.fasta' will look something like:")
    print("\n >ACCESSION")
    print(" LEFT FLANK SEQUENCE + MOTIF(the BLAST hit) + RIGHT FLANK SEQUENCE")
    print("\nNOTE: Individual '.fasta' files will be generated and not a multifasta because mfold does not accept multifasta format.\n")
    return

from pyfaidx import Fasta
record_index = Fasta("sequence.fasta")
accessions = [] ##Declaring lists.
start = []
end = []
ctr = 0

welcome()

for x in open("gene.txt"):
    accessions.append(x.replace("\n","")) ##Fetching accessions from the file.

for x in open("start.txt"):
    start.append(int(x.replace("\n",""))) ##Fetching start coordinates from the file.

for x in open("end.txt"):
    end.append(int(x.replace("\n",""))) ##Fetching end coordinates from the file.

flank = int(input("\n\nEnter the flank length : ")) ##Input flank length for precursors.

mot_strt = open("motif_start","w")
mot_end = open("motif_end","w")

for x in accessions:
    try:
        motif = str(record_index[x][start[ctr]-1:end[ctr]].seq)
        lflank = str(record_index[x][start[ctr]-flank-1:start[ctr]-1].seq)
        rflank = str(record_index[x][end[ctr]:end[ctr]+flank].seq)
        seq = lflank + motif + rflank
        ##motif_start = seq.find(motif) This will apply to other cases where we want to locate exact motif in the seq.
        ##MOTIF start will be flank here as we know the flank length.
        mot_strt.write(f"{str(flank)}\n")
        mot_end.write(f"{str(flank+len(motif))}\n")
        #motif_end = motif_start + len(motif)
        file=open(f"prec{ctr+1}.fasta","w")
        file.write(f">pni_yj_precursor_recordnum_{ctr+1}_coord_{start[ctr]}:{end[ctr]}\n")
        file.write(seq)
        file.close()
        print(f"\n******************************** ITERATION # {ctr+1} ********************************")
        print(f"\nGENE ACC: {x}")
        print(f"\nMotif: {motif}")
        print(f"Left Flank: {lflank}")
        print(f"Right FLank: {rflank}")
        print(f"The motif coordinate is: {flank} - {flank+len(motif)}\n")
        print(f"The length of motif is: {len(motif)}")
        #motif = len(str(record_index[x].seq[start[ctr]:end[ctr]]))
        # print(f"The motif coordinate is !!TEST!!{lflank_len} : {tot_len - rflank_len}")
        ctr += 1
    except:
        if ctr != len(accessions)-1:
            err()
            token = input(("\n\nDo you wish to ignore the error and continue trying? [y/n] "))
            if token == "y" or token == "yes" or token == "Y":
                ctr += 1
            else:
                exit()

mot_end.close()
mot_strt.close()

print("\n\n")
print("*" * 30)
print("All done!")
print("*" * 30)
print(f"\n\nThe total number of precursors generated are {ctr}.")
print(f"The last precursor's gene ID was {x} and it's number was {ctr}.")
print(f"The last start coordinate was: {start[ctr-1]} and end coordinate was: {end[ctr-1]}")
print("Please verify these with your BLAST results to confirm the veracity of this operation.\n\n")
print("*" * 30)
