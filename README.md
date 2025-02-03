# A3Partitioner

A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions from sequence alignments.

## Installation

You can install A3Partitioner using conda. First, ensure you have the required channels:

```bash
conda config --add channels bioconda
```

Then install A3Partitioner:

```bash
conda create -n a3partitioner -c bioconda a3partitioner -y && 
conda activate a3partitioner
```

Alternatively, you can install from source:

```bash
git clone https://github.com/DaanJansen94/a3partitioner
cd a3partitioner
pip install .
```

## Usage

### Options

- `-partition`: Type of partition to create [apobec, non-apobec, both]
- `-i, --input`: Input FASTA alignment file
- `-o, --output`: Output FASTA file
- `--analyze`: Generate detailed APOBEC site analysis

### Examples

1. Create APOBEC3 partition:
```bash
A3Partitioner -partition apobec -i input_aln.fasta -o output_aln.fasta
```

2. Create non-APOBEC partition:
```bash
A3Partitioner -partition non-apobec -i input_aln.fasta -o output_aln.fasta            
```

2. Create both partitions and analysis:
```bash
A3Partitioner -partition both -i input_aln.fasta -o output_aln.fasta --analyze
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
