import argparse
from .core import (
    create_apobec_partition,
    create_non_apobec_partition,
    count_motifs,
    analyze_apobec_sites,
    write_apobec_site_analysis
)
from Bio import SeqIO
import os

def main():
    parser = argparse.ArgumentParser(description="Create APOBEC3 and non-APOBEC3 partitions from sequence alignments")
    parser.add_argument("-partition", choices=["apobec", "non-apobec", "both"], 
                       default="both", help="Type of partition to create")
    parser.add_argument("-i", "--input", required=True,
                       help="Input FASTA alignment file")
    parser.add_argument("-o", "--output", required=True,
                       help="Output FASTA file")
    parser.add_argument("--analyze", action="store_true",
                       help="Generate detailed APOBEC site analysis")
    
    args = parser.parse_args()
    
    # Read sequences
    records = list(SeqIO.parse(args.input, "fasta"))
    sequences = [str(record.seq) for record in records]
    
    base_name = os.path.splitext(args.output)[0]
    
    if args.partition in ["apobec", "both"]:
        apobec_partition, apobec_sites = create_apobec_partition(sequences)
        apobec_file = f"{base_name}_APOBEC3.fasta" if args.partition == "both" else args.output
        with open(apobec_file, 'w') as f:
            for record, seq in zip(records, apobec_partition):
                f.write(f">{record.id}\n{seq}\n")
    
    if args.partition in ["non-apobec", "both"]:
        if args.partition == "non-apobec":
            apobec_partition, _ = create_apobec_partition(sequences)
        non_apobec_partition = create_non_apobec_partition(sequences, apobec_partition)
        non_apobec_file = f"{base_name}_non_APOBEC3.fasta" if args.partition == "both" else args.output
        with open(non_apobec_file, 'w') as f:
            for record, seq in zip(records, non_apobec_partition):
                f.write(f">{record.id}\n{seq}\n")

if __name__ == "__main__":
    main()
