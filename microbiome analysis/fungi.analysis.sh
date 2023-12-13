#!/bin/bash

# Import data
qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path ./fungi.manifest_paired_end.tsv \
  --output-path fungi.demux-paired-end.qza \
  --input-format PairedEndFastqManifestPhred33V2

# Import reference
# download fungi reference from UNITE and save as fungi.reference.fa
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path fungi.reference.fa \ 
  --output-path fungi.reference-seqs.qza

# Import taxonomy
#get and save taxonomy file as fungi.reference.taxonomy.txt from unite as above
qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-path fungi.reference.taxonomy.txt \
  --output-path fungi.reference.taxonomy.qza

# Dada2 denoise
qiime dada2 denoise-paired \
  --i-demultiplexed-seqs fungi.demux-paired-end.qza \
  --p-trim-left 10 \
  --p-trunc-len 200 \
  --p-n-threads 16
  --o-representative-sequences fungi.rep-seqs.qza \
  --o-table fungi.table.qza \
  --o-denoising-stats fungi.denoising.stats.qza

# Generate OTU table
qiime vsearch cluster-features-closed-reference \
  --i-sequences fungi.rep-seqs.qza \
  --i-table fungi.table.qza \
  --i-reference-sequences fungi.reference-seqs.qza \
  --p-threads 16 \
  --p-perc-identity 0.85 \
  --o-clustered-table fungi.table-otus.qza \
  --o-clustered-sequences fungi.rep-seqs-otus.qza \
  --o-unmatched-sequences fungi.unmatched.qza

#make taxonomy file
qiime feature-classifier classify-consensus-vsearch \
  --i-query fungi.rep-seqs-otus.qza \
  --i-reference-reads silva-138-99-seqs.qza \
  --i-reference-taxonomy silva-138-99-tax.qza \
  --p-perc-identity 0.85 \
  --p-threads 16 \
  --o-classification taxonomy.qza \
  --o-search-results search-results.qza
