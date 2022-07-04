### Install from scratch
#### 1. Install miniconda (see 1' for alternative)
* Go to https://docs.conda.io/en/latest/miniconda.html#linux-installers, download the Linux installers Python 3.8 file.  
(e.g. [Miniconda3-py38_4.12.0-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh))  
* Install the file by `bash Miniconda3-py38_4.12.0-Linux-x86_64.sh`.
    * Follow the prompts on the installer screens. Just use all default option.
    * On Farnam, with default option, your miniconda core directory will be in `home` and all python package will be in `project`.
* Close and re-open the terminal. Check if conda is successfully installed by `which python`. This should be under your miniconda core directory.
* (Highly recommand) Install Mamba by `conda install mamba -n base -c conda-forge`. The conda package manager will freeze if your conda environment gets too big.

#### 1' Using miniconda module on Farnam
* `module load miniconda`
* You probably could not use mamba with this. Just use `conda` in all following parts.

#### 2. Create conda environment and install basic packages
*If you did not install mamba, replace all `mamba` by `conda` in all following parts.*
* `mamba create -n rpgQTL python=3.8`. You can change the environment name `rpgQTL` to anything you want.
* `conda activate rpgQTL`. Confirm the activation by `which python`. This should be under the rpgQTL environment folder.
* `mamba install numpy=1.20.1 scipy=1.7.0 pandas=1.2.3 matplotlib=3.3.4 jupyter ipython rpy2=3.4.2`

#### 3. Install pytorch
* `mamba install cudatoolkit=11.1.1 pytorch=1.8.0 torchaudio=0.8.0 torchvision=0.2.2 -c pytorch`

#### 4. Install tensorQTL
* `which pip`. Make sure we are using the pip under rpgQTL environment folder.
* `pip install tensorqtl==1.0.5`

#### 5. Install rpgQTL.py
* (Easy way) Simply copy `rpgQTL.py` file into your working directory. 
* (Advanced way) (TO BE DONE) Install rpgQTL as package.

#### 6. Running the scripts in general (You can skip this if you just want to run the example)
* To run any scripts in the rpgQTL environment and make used of GPU, add the following before your `python file.py`:
  * `source /home/jg2447/miniconda3/etc/profile.d/conda.sh; conda activate tensorQTL; module load CUDA/11.1.1-GCC-10.2.0; module load cuDNN/8.0.5.39-CUDA-11.1.1;`
* For Farnam, add `#SBATCH --gpus-per-node titanv:1` to the sbatch jobfile to indicate using of one titanv gpu.
  * You can change the name titanv to other gpu names (see below).
  * Or you can change it to `#SBATCH --gpus-per-node 1` to require any type of gpu.
* `sinfo -N -O NodeHost:.9,Partition:.19,AllocMem:.11,FreeMem:.11,Memory:.11,CPUsState:.15,Gres:.22,GresUsed:.30 | grep "pi_gerstein_gpu\|HOSTNAMES" | (sed -u 1q; sort -k1,1)`
  * You can use this command to check all pi_gersetin_gpu node current states. 
  * The available gpu names are also shown.

#### 7. Running the example
* In `rpg_dsq.sh` line 9: replace the two `/gpfs/slayman/pi/gerstein/jg2447/GTEX/scripts_run_rpg` to your absolute working folder path (you can get this by `pwd -P`)
* Submit job: `sbatch rpg_dsq.sh`
* For each job, this will create a folder under the current working folder for the output.
