
This repository contains custom scripts used for analysis of CRISPR-UMI screen data for publication "ZFP462 prevents aberrant non-lineage specific gene expression and promotes tissue and locus-specific G9A/GLP-dependent heterochromatin".

This is not a "plug and play" pipeline but rather serves documentary purpose


###############################################
1) Use bowtie to map sgRNAs
###############################################

fastx-toolkit/0.0.13
bowtie/0.12.9

Example cmd line:
bowtie -m 1 --best --strata -S -p 16 -v 1 45kguides --max 30k_1_bw1MM.notUniq.fastq <( bamToFastq -i CAF25ANXX_1_07-02-2017.bam -fq /dev/stdout | fastx_trimmer -Q33 -l 20 ) | samtools view -S -F 0x0004 - > 30k_1bw1MM.sam


######################################################
2) get barcode and indices from original data file
######################################################

samtools view -h C……….bam | cut -f 1,10,12,14 >30k_1_short.sam
0_merge_bowtieresults_CrScsam.py


#####################################################
3) Generate a python dictionary containing all data 
#####################################################
1_read_clones_barcode mapping.py


###################################################
4) remove sequencing errors called "barcode shadows" for improved clone calling and generate Read tables for downstream analysis (e.g. Gene enrichment running MAGeCK)
###################################################
2_clone calling_read table gen.py
