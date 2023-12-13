#!/bin/bash

# Import data
qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path ./bacteria.manifest_paired_end.tsv \
  --output-path bacteria.demux-paired-end.qza \
  --input-format PairedEndFastqManifestPhred33V2

# Import reference
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path bacteria.reference.fa \
  --output-path bacteria.reference-seqs.qza
#import taxonomy
wget -o silva-138-99-tax.qza https://data.qiime2.org/2021.4/common/silva-138-99-tax.qza

# Deblur denoise
qiime deblur denoise-16S \
  --i-demultiplexed-seqs bacteria.demux-paired-end.qza \
  --p-trim-length 120 \
  --p-sample-stats \
  --p-jobs-to-start 16 \
  --o-representative-sequences bacteria.rep-seqs.qza \
  --o-table bacteria.table.qza \
  --o-stats bacteria.denoising-stats.qza

# Generate OTU table
qiime vsearch cluster-features-closed-reference \
  --i-sequences bacteria.rep-seqs.qza \
  --i-table bacteria.table.qza \
  --i-reference-sequences bacteria.reference-seqs.qza \
  --p-threads 16 \
  --p-perc-identity 0.85 \
  --o-clustered-table bacteria.table-otus.qza \
  --o-clustered-sequences bacteria.rep-seqs-otus.qza \
  --o-unmatched-sequences bacteria.unmatched.qza

#make taxonomy file
qiime feature-classifier classify-consensus-vsearch \
  --i-query bacteria.rep-seqs-otus.qza \
  --i-reference-reads silva-138-99-seqs.qza \
  --i-reference-taxonomy silva-138-99-tax.qza \
  --p-perc-identity 0.85 \
  --p-threads 16 \
  --o-classification taxonomy.qza \
  --o-search-results search-results.qza
