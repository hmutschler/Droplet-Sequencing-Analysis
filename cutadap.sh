#!/bin/bash
source "$(conda info --base)/etc/profile.d/conda.sh"

# Define an array of variable names
variables=("Ref" "Sup" "Pel")

# Loop through each variable
for var in "${variables[@]}"; do
    # Define input and output file names based on the variable
    input_file_1="../raw_data/${var}_R1.fastq"
    input_file_2="../raw_data/${var}_R2.fastq"
    trimmed_output_file_1="${var}_trim_1.fastq"
    trimmed_output_file_2="${var}_trim_2.fastq"

    # Run cutadapt to trim adapters
    conda activate cutadapt-env
    cutadapt -a "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA" -A "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT" --discard-untrimmed -o "$trimmed_output_file_1" -p "$trimmed_output_file_2" "$input_file_1" "$input_file_2"
    conda deactivate
    # Run FastQC on the trimmed output file
    conda activate fastqc-env
    fastqc "$trimmed_output_file_1"
    fastqc "$trimmed_output_file_2"
    conda deactivate
done

echo "Processing complete for all variables."
