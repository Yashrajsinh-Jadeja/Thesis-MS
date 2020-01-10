
# Thesis-MS
### A repository for some scripts and tools that I wrote during my M.S thesis/dissertation work in the genomics domain.
---
### Table of Contents

1. [What is this about and will it suit my workflow?](#what-is-this-about-and-will-it-suit-my-workflow)
2. [Prerequisites](#prerequisites)
3. [Instructions](#instructions)
---
#### What is this about and will it suit my workflow?
 This is a script that sort of automates the process of fetching BLAST hits along with their flanking region for creating precursor microRNA sequences. 

Furthermore, it will fold the precursor sequences into secondary RNA structures and allow the users to highlight the bases to their own liking. (intended for highlighting miRNA and miRNA* in the 2<sup>o</sup> structure.

This script can be a workaround for batch-processing highlighting mfold structures as the standalone mfold does not have a highlight feature similar to it's web-server.   

> *Note : This workflow has been designed for short microRNA sequences. If you wish to use this script to fetch other nucleotide sequences just for the flanking regions, you most certainly can.* 

---
#### Prerequisites

1. A Linux system.
2. Python version 3.x.x.
3. [pyfaidx](https://pythonhosted.org/pyfaidx/#installation)
4. BLAST results.
5. [mfold/UNAFOLD.](http://unafold.rna.albany.edu/?q=mfold/download-mfold) (preferably v. 3.6)
6. [VARNA.](http://varna.lri.fr/index.php?lang=en&page=downloads&css=varna) (Visualization Applet for RNA)
7. Tons of patience and a lot of sleep.

> *Note : This program has been tested on Ubuntu 16.x and 18.04 with 64-bit architecture. You __will__ need to install the 'pyfaidx' package for Python 3 and **not** Python 2.* 

---
#### Instructions
1. Take a deep breath.

2. After installing the appropriate prerequisites, move the "**flanking_updated_vx.py**" Python script to your work folder.

3. Create **3 files separately** with each containing your **sequence accession** (subject or reference), **start coordinates** and **end coordinates** respectively from your BLAST results spreadsheet/table.

4. Name the files accordingly as mentioned in the script. (Note: Files as command line parameters will be added soon)
> **The file containing the Gene Accession list from the BLAST results (Subject/Genome) has to be named 'gene.txt'.**

> **The file containing the Start Coordinates list from the BLAST results (Subject/Genome) has to be named 'start.txt'.** 

>**The file containing the End Coordinates list from the BLAST results (Subject/Genome) has to be named 'end.txt'.** 

>*(if you have errors with the naming due to Windows/Linux encoding/line-ending you can name the file according to your own choice and change the filename from the code)*  

5. Run the script with 
`python3 flanking_updated_v2.py`
6. Set the appropriate flank length for your sequences.
7. *Don't* grab a coffee because this is *not* going to take a while. It's rather quick.
---
#### TLDR
###### _(What goes in)_ 3 files containing gene accessions, start coordinates and end coordinates respectively and a ".fasta" reference file.
###### _(What comes out)_ ".fasta" files containing precursors.  

### TODO
**Learn to write better documentation, update the terrible documentation, tweak the code for better performance, fix terrible variable names.**


> Written with [StackEdit](https://stackedit.io/).
