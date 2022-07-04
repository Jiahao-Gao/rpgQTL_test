#!/bin/bash
#SBATCH --array 0-11
#SBATCH --job-name rpg
#SBATCH --partition pi_gerstein_gpu
#SBATCH --time 3-23:59:59
#SBATCH --mem-per-cpu 40G
#SBATCH --gpus-per-node titanv:1

/ysm-gpfs/apps/software/dSQ/1.05/dSQBatch.py --job-file /gpfs/slayman/pi/gerstein/jg2447/GTEX/scripts_run_rpg/rpg_joblist --status-dir /gpfs/slayman/pi/gerstein/jg2447/GTEX/scripts_run_rpg
