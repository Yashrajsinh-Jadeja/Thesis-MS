#This shell-script had to be written as the "shopt -s extglob" does not work in the python script.
#NOTE: ALWAYS RUN THIS IN AN EXPERIMENT FOLDER AS THIS SCRIPT IS DESIGNED TO REMOVE EVERYTHING THAT ISN'T THE BELOW MENTIONED FILES.
shopt -s extglob
rm !(*.py|*.fasta|motif*|*.ct|*.EPS|*.jar|*.sh|*.png)
echo "***Removed redundant files***"
