#!/bin/bash

# Directory containing paired-end FASTQ files
fastq_dir="./"

# Create a manifest file for paired-end data
echo -e "sample-id\tforward-absolute-filepath\treverse-absolute-filepath" > manifest_paired_end.tsv

for file1 in "$fastq_dir"/*_1.fastq.gz; do
    filename=$(basename -- "$file1")
    sample_id="${filename%_1.fastq.gz}"
    file2="${file1/_1.fastq.gz/_2.fastq.gz}"
    echo -e "$sample_id\t$(realpath "$file1")\t$(realpath "$file2")" >> bacteria.manifest_paired_end.tsv
done

echo "Manifest file for paired-end data created: manifest_paired_end.tsv"
