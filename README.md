Custom code and scripts for the publication **"DNA affects the phenotype of fuel-dependent coacervate droplets"** by Corbin Machatzke, Anna-Lena Holtmannspoetter, Hannes Mutschler and Job Boekhoven (to be published).

The bash scripts (`.sh`) can be run in a bash environment and allow for processing of raw sequencing data. The Python scripts (`.ipynb`; `.py`) can be run in Python (we used Jupyter Notebook) and will generate the relevant output data and figures used in the publication.

- **cutadap.sh:** Removes custom adaptor oligos from paired-end sequencing reads and saves the new `.FASTQ` files, then performs quality control using FastQC.  

- **length_filtered.sh:** Filters reads produced by `cutadap.sh` for an exact length of 30, removing double-, triple-, or no-insert ligation products, followed by FastQC.  

- **calc_mfe.sh:** Calculates the minimum free energy (MFE) of folding using ViennaRNA Package’s RNAfold algorithm, then extracts the energy values from the output and stores them separately.  

- **script_GG.ipnyb:** calculates the number of sequences containing at least 2 or 3 Gs at the beginning and/or end of a sequence and produces corresponding figures.

- **script_G_A_stretches.ipynb:** calculates the number of sequences containing at least 5 or 7 stretches of consecutive As or Gs in a single sequence and produces the corresponding figures. 

- **script_pbc.ipynb:** Calculates the base content per position (PBC) of all sequences and produces the output figures used in the publication.  

- **script_mfe.ipynb:** Produces the output figure for minimum free energy of the publication.  

- **script_motifs.ipynb:** Produces the table containing all sequence motifs found in MEME Suite's STREME analysis.

- **numerical_generator.py:** Numerical generator that calculates probabilities of at least 7 consecutive repeats of the same nucleotide in a sequence.

- **FRAP-Macro-2.py:** Script for analysis of microscopy images regarding fluorescence intensity.
