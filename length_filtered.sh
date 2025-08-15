#!/bin/bash
source "$(conda info --base)/etc/profile.d/conda.sh"

# Define an array of variable names
variables=("Ref" "Sup" "Pel")

# Loop through each variable
for var in "${variables[@]}"; do
    # Define input and output file names based on the variable
    input_file_1="../cut_adap/${var}_trim_1.fastq"
    output_file_1="${var}_fil_1.fastq"
    input_file_2="../cut_adap/${var}_trim_2.fastq"
    output_file_2="${var}_fil_2.fastq"

    # Run seqkit to filter for length
    conda activate seqkit-env
    seqkit seq -m 30 -M 30 ${input_file_1} > ${output_file_1}
    seqkit seq -m 30 -M 30 ${input_file_2} > ${output_file_2}
    conda deactivate

    # Run FastQC on the filtered output file
    conda activate fastqc-env
    fastqc "$output_file_1"
    fastqc "$output_file_2"
    conda deactivate
done

echo "Processing complete for all variables."
