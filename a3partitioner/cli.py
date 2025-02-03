import argparse
from .core import create_partition

def main():
    parser = argparse.ArgumentParser(
        description='Create APOBEC3 and non-APOBEC3 partitions from sequence alignments'
    )
    parser.add_argument(
        '-partition',
        choices=['apobec', 'non-apobec', 'both'],
        help='Type of partition to create'
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input FASTA alignment file'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output FASTA file'
    )
    
    args = parser.parse_args()
    create_partition(args)

if __name__ == "__main__":
    main()
