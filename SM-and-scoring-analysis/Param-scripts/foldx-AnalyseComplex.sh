#!/bin/sh

#SBATCH --job-name=asr_ac_foldx
#SBATCH --partition=standard
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=48
#SBATCH --error=/scratch/chinmay/ananth/job.%J.err
#SBATCH --output=/scratch/chinmay/ananth/job.%J.out

cd $SLURM_SUBMIT_DIR

/home/chinmay/bin/foldx --command=AnalyseComplex --analyseComplexChains=A,B --pdb-list=/scratch/chinmay/ananth/SM-results/foldx_results/foldx_repair_pdb/pdb_filenames.txt --pdb-dir=/scratch/chinmay/ananth/SM-results/foldx_results/foldx_repair_pdb --output-dir=/scratch/chinmay/ananth/AC_results
