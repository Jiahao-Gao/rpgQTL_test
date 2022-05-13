# rpgQTL
Regions per gene (rpg) QTL

This is a package based on [TensorQTL](https://github.com/broadinstitute/tensorqtl) with modifications.  
rpgQTL allows user to specify regions (could be discontinuous) for each gene. Only SNPs in the corresponding regions will be used for corresponding gene cis-eQTL calling.

### Install
Install directly from this repository:
```
$ git clone git@github.com:gaotc200/rpgQTL.git
$ cd rpgQTL
$ pip install -r install/requirements.txt .
```
