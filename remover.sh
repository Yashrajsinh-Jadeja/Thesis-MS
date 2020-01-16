#This shell-script had to be written as the "shopt -s extglob" does not work in the python script. This is just a workaround.
#NOTE: ALWAYS RUN THIS IN AN EXPERIMENTAL FOLDER WITHOUT CRUCIAL DATA AS THIS SCRIPT IS DESIGNED TO REMOVE EVERYTHING THAT ISN'T THE BELOW MENTIONED FILES/FILE EXTENSIONS.
shopt -s extglob
rm !(*.py|*.fasta|motif*|*.ct|*.EPS|*.jar|*.sh|*.png)
echo "***Removed redundant files***"
