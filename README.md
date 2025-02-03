# A3Partitioner

A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions from sequence alignments.

## Installation

### Option 1: Using Conda
First, ensure you have the required channels:

```bash
conda config --add channels bioconda
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

## License

This project is licensed under the MIT License.
