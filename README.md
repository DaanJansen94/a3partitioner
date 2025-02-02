# A3Partitioner

A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions from sequence alignments.

## Installation

You can install A3Partitioner using conda. First, ensure you have the required channels:

```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

Then install A3Partitioner:

```bash
conda create -n a3partitioner
conda activate a3partitioner
conda install a3partitioner
```

Alternatively, you can install from source:

```bash
git clone https://github.com/DaanJansen94/a3partitioner
cd a3partitioner
pip install .
```

## Usage

Basic usage:

```bash
A3Partitioner -partition apobec -i input.fasta -o output.fasta
```

### Options

- `-partition`: Type of partition to create [apobec, non-apobec, both]
- `-i, --input`: Input FASTA alignment file
- `-o, --output`: Output FASTA file
- `--analyze`: Generate detailed APOBEC site analysis

### Examples

1. Create APOBEC3 partition:
```bash
A3Partitioner -partition apobec -i AllGenomes_aln.fasta -o AllGenomes_aln_APOBEC3.fasta
```

2. Create both partitions and analysis:
```bash
A3Partitioner -partition both -i AllGenomes_aln.fasta -o AllGenomes_aln --analyze
```

## Output Files

When using `-partition both`, the tool will create:
- `{output}_APOBEC3.fasta`: APOBEC3 partition
- `{output}_non_APOBEC3.fasta`: non-APOBEC3 partition

When using `--analyze`, additional files are created:
- `{output}_motif_counts.txt`: APOBEC motif statistics
- `{output}_APOBEC_conversions.txt`: Detailed APOBEC site analysis

## License

This project is licensed under the MIT License.
