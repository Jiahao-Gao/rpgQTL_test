import os
import pandas as pd
import tensorqtl
from tensorqtl import genotypeio, post
import rpgQTL
import sys


infile = sys.argv[1]
gene_id_ver_rm = int(sys.argv[2])
tissue = sys.argv[3]
out_dir = sys.argv[4]

prefix = "RPG"
s_window = 0
os.makedirs(out_dir, exist_ok=True)

### read data
plink_prefix_path = '../data/GTEX_download/GTEx_Analysis_v8_genotype/GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_Analysis_Freeze.SHAPEIT2_phased.MAF01'
expression_bed = '../data/GTEX_download/GTEx_Analysis_v8_eQTL_expression_matrices/%s.v8.normalized_expression.bed.gz' % tissue
covariates_file = '../data/GTEX_download/GTEx_Analysis_v8_eQTL_covariates/%s.v8.covariates.txt' % tissue

phenotype_df, phenotype_pos_df = tensorqtl.read_phenotype_bed(expression_bed)
covariates_df = pd.read_csv(covariates_file, sep='\t', index_col=0).T
pr = genotypeio.PlinkReader(plink_prefix_path, select_samples=phenotype_df.columns)
genotype_df = pr.load_genotypes()
variant_df = pr.bim.set_index('snp')[['chrom', 'pos']]

### if rpg gene name is not ID.ver, remove .ver from gtex gene name
if gene_id_ver_rm:
    genes = phenotype_df.index.values
    genes = [ii.split(".")[0] for ii in genes]
    phenotype_df.index = genes
    genes = phenotype_pos_df.index.values
    genes = [ii.split(".")[0] for ii in genes]
    phenotype_pos_df.index = genes

### RPG file
rpg_df = pd.read_csv(infile, sep="\t", header=None)

### nominal run
rpgQTL.run_nominal(genotype_df, variant_df, phenotype_df, phenotype_pos_df, covariates_df,
                   rpg_df, l_window=2000000, s_window=s_window, NonHiCType='remove',
                   output_dir=out_dir, prefix=prefix)

### permutation run
egenes_df = rpgQTL.run_permutation(genotype_df, variant_df, phenotype_df, phenotype_pos_df, covariates_df, 
                                   rpg_df, l_window=2000000, s_window=s_window, NonHiCType='remove', seed=123456)

#### calculate q-values
post.calculate_qvalues(egenes_df, fdr=0.05, qvalue_lambda=0.85)
egenes_df.to_csv("%s/%s.egenes.tsv" % (out_dir, prefix), index=True)


### significant pairs
pairs_df = post.get_significant_pairs(egenes_df, "%s/%s" % (out_dir, prefix))
pairs_df.to_csv("%s/%s.sig_pairs.tsv" % (out_dir, prefix), index=False)


### independent eQTL
indep_df = rpgQTL.run_independent(genotype_df, variant_df, egenes_df, phenotype_df, phenotype_pos_df, covariates_df, 
                                  rpg_df, l_window=2000000, s_window=s_window, NonHiCType='remove', seed=123456)
indep_df.to_csv("%s/%s.indep.tsv" % (out_dir, prefix), index=False)

