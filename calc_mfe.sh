#!/bin/bash

file_list="file_list.txt"
rnafold_output_dir="rnafold_output"

mkdir -p $rnafold_output_dir

while IFS= read -r input_fasta; do
    filename=$(basename "$input_fasta")

    rnafold_output="$rnafold_output_dir/${filename%.fasta}_rnafold.txt"
    deltaG_output="$rnafold_output_dir/${filename%.fasta}_deltaG.txt"

    RNAfold -i "$input_fasta" --noPS --noconv -P DNA > "$rnafold_output"
    grep "(" "$rnafold_output" > "$deltaG_output"

    echo "Processed RNAfold and extracted deltaG values for $output_fasta -> $rnafold_output"

    # Python processing block
    python3 <<EOF
# Define file paths directly from bash variables
deltaG_file = "${deltaG_output}"
dot_bracket_file = "./${rnafold_output_dir}/${filename%.fasta}_dot_bracket.txt"
energy_file = "./${rnafold_output_dir}/${filename%.fasta}_energy.txt"

# Read input file and process line by line
with open(deltaG_file, 'r') as infile, \
     open(dot_bracket_file, 'w') as dot_out, \
     open(energy_file, 'w') as energy_out:
    for line in infile:
        # Extract first 60 characters (dot-bracket notation)
        dot_bracket = line[:30].strip()
        dot_out.write(dot_bracket + '\n')

        # Extract energy value starting from character 61 onward,
        # stripping spaces and brackets (retaining only numeric parts)
        energy_value_raw = line[31:]  # Start reading from character 61 onward
        energy_value = ''.join(c for c in energy_value_raw if c.isdigit() or c == '.' or c == '-')
        energy_out.write(energy_value + '\n')

print(f"Generated {dot_bracket_file} and {energy_file}")
EOF

done < "$file_list"
