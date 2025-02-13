# A3Partitioner

A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions from sequence alignments.

## Background
Literature indicates that an overwhelming majority of mutations found in monkeypox viral genomes are a result of deaminase editing, which provides a distinct APOBEC3 signature in the genomes (doi: 10.1126/science.adg8116). When performing evolutionary analysis of MPXV on relatively short timescales, it is therefore unlikely that a significant number of non-APOBEC3 mutations, which arise from error-prone polymerases, will accumulate. Given this, one can extract the APOBEC3 partition from the nucleotide alignment and perform phylogenetic analysis with this partition to exclude bias from artificially introduced mutations (e.g., sequencing or bioinformatics errors).

## How It Works
This tool creates two distinct partitions from a nucleotide alignment:

1. **APOBEC3 Partition:**
   - Includes sites with putative APOBEC3 modifications (C → T or G → A substitutions in specific dinucleotide contexts)
   - All other sites are masked as ambiguous nucleotides
   - Can be used as input for ML or Bayesian phylogenetic analyses, aiming to remove bias from artificially introduced mutations

2. **Non-APOBEC3 Partition:**
   - Contains all sites except those with APOBEC3 target sites
   - APOBEC3 target sites are masked
   - Serves as a complement to the first partition

## Installation

### Option 1: Using Conda
First, ensure you have the required channels:

```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

Then install A3Partitioner:

```bash
conda create -n a3partitioner -c bioconda a3partitioner -y 
conda activate a3partitioner
```

### Option 2: From Source Code
Before installing from source, ensure you have:
1. Python 3.6 or higher installed
   ```bash
   # Check your Python version
   python3 --version
   ```

2. Biopython package installed
   ```bash
   # Install Biopython if you don't have it
   pip install biopython
   ```

Then install A3Partitioner:

```bash
git clone https://github.com/DaanJansen94/a3partitioner
cd a3partitioner
./install.sh
```

## Usage

### Options

- `-partition`: Type of partition to create [apobec, non-apobec, both]
- `-i, --input`: Input FASTA alignment file
- `-o, --output`: Output FASTA file

### Examples

1. Create APOBEC3 partition:
```bash
A3Partitioner -partition apobec -i input_aln.fasta -o output_aln.fasta
```

2. Create non-APOBEC partition:
```bash
A3Partitioner -partition non-apobec -i input_aln.fasta -o output_aln.fasta            
```

3. Create both partitions and analysis:
```bash
A3Partitioner -partition both -i input_aln.fasta -o output_aln.fasta
```

## Output Files

When using `-partition both`, the tool will create:
- `{output}_APOBEC3.fasta`: APOBEC3 partition
- `{output}_non_APOBEC3.fasta`: non-APOBEC3 partition

## Citation

If you use EbolaSeq in your research, please cite:

```
Jansen, D., & Vercauteren, K. (2025). a3partitioner: A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions from sequence alignments (Version v0.1.0) [Computer software]. https://doi.org/10.5281/zenodo.14851870
```

## License

This project is licensed under MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any problems or have questions, please open an issue on GitHub.
