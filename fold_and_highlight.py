##ID 2
##This script will trigger the mfold and VARNA applications according to the sequences.
##THE REMOVER.SH bash script had to be created seperately because the commands run in a subshell and "shopt -s extglob" option does not work in a python script.
### DO NOT RUN THIS SCRIPT ANYWHERE BUT AN EXPERIMENTAL FOLDER AS IT WILL REMOVE ALL THE FILES EXCEPT FOR FEW.
##GNU General Public License v3.0
##Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
## 12 January 2020 Yashrajsinh Jadeja

import os
choice = int(input("Enter the total number of files to be processed."))

start = []
end = []

for x in open("motif_start"):
    start.append(x.replace("\n",""))

for x in open("motif_end"):
    end.append(x.replace("\n",""))

#os.system("echo why; shopt -s extglob")
for x in range(1,choice+1):
	os.system(f'mfold SEQ"=prec{x}.fasta"')
	os.system("bash remover.sh")
	#os.system('rm -v !(*.py|*.fasta|*coord|*.ct|*.EPS|*.jar')
	os.system(f'java -cp VARNAv3-93.jar fr.orsay.lri.varna.applications.VARNAcmd -i prec{x}_4.ct -o prec{x}.EPS -highlightRegion "{start[x]}-{end[x]}:fill=#FF0000"')

print("*" * 13)
print("All Done!")
print("*" * 13)
