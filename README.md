# rpgQTL
Regions per gene (rpg) QTL

This is a package based on [TensorQTL](https://github.com/broadinstitute/tensorqtl) with modifications (cis-eQTL module only).  
Instead of a single parameter of the cis-window size, rpgQTL allows user to specify regions (could be discontinuous) for each gene. Only SNPs in the corresponding regions will be used for corresponding gene cis-eQTL calling.

### Install
Install directly from this repository:
```
$ git clone git@github.com:gaotc200/rpgQTL.git
$ cd rpgQTL
$ pip install -r install/requirements.txt .
```

### Requirement
```
numpy
pandas
tensorqtl
```
Notice that tensorqtl depends on pandas-plink, pytorch and other packages. For furthur details, see the installing instruction in [tensorqtl](https://github.com/broadinstitute/tensorqtl) or [pytorch](https://pytorch.org/get-started/locally/).

### Example
See `example.ipynb` for the example script.

###### Input files
`plink_prefix_path`: Genotype VCF in PLINK format  
`phenotype_df, phenotype_pos_df`: expression file  
`covariates_df`: covariates (e.g. PEER factor, sex, etc.)  
For details about the above files, see instruction in [tensorqtl](https://github.com/broadinstitute/tensorqtl)  

`rpg_df`: `pandas.DataFrame` or `str`  
- If `pandas.DataFrame`, this would be one large dataframe. Each row correspond to one candidate genomic region for eqtl detection of one gene. Each gene could contain multiple regions (rows). The first four columns should be:  
  - col1: chromosome  
  - col2: start of the region  
  - col3: ends of the region  
  - col4: gene name  
- If `str`, this would be the path to a directory. For each file in the directory, the file name is a gene name and the file contains the regions for that gene. The format is the same as the above pandas.DataFrame.

###### Parameters
`l_window` (int; default 2000000):  
The max boundary of cis-window. Only regions within this cis-window will be consider as valid regions. You should consider trans-eqtl calling methods if your interested SNPs are located outside of this window size.  
`s_window` (int; default 0):  
A fix cis-window for all genes that will always be included, even if they are not included in the rpg_df. Setting s_window to 1000000 and rpg_df to empty dataframe will be equivalent to the original cis-eqtl calling using tensorqtl with window=1000000.  
`NonHiCType` ('remove', 'l_window' or 's_window'):  
Different ways to deal with genes that have genotype and expression data, but no candidate regions.
- 'remove': The genes will be completely removed from calculation.  
- 'l_window': All SNPs within the cis-window defined by 'l_window' will be used.  
- 's_window': All SNPs within the cis-window defined by 's_window' will be used.  

Other parameters are the same as those in the corresponding functions from `tensorqtl`.
