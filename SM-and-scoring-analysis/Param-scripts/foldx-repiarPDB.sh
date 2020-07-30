#!/bin/sh

#SBATCH --job-name=ananth_repair_pdb
#SBATCH --partition=standard
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=48
#SBATCH --error=/scratch/chinmay/ananth/job.%J.err
#SBATCH --output=/scratch/chinmay/ananth/job.%J.out

cd $SLURM_SUBMIT_DIR

/home/chinmay/bin/foldx --command=RepairPDB --pdb-list=/scratch/chinmay/ananth/SM-results/ananth_pdb_filenames.txt --pdb-dir=/scratch/chinmay/ananth/SM-results --output-dir=/scratch/chinmay/ananth/SM-results/foldx_results
