#!/usr/bin/env python3

import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import defaultdict

def count_motifs(sequence):
    """Count APOBEC (TC and GA) and non-APOBEC dinucleotides in the sequence."""
    apobec_count = sequence.count('TC') + sequence.count('GA')
    total_dinucleotides = len(sequence) - 1
    non_apobec_count = total_dinucleotides - apobec_count
    total_bases = len(sequence)
    apobec_percentage = (apobec_count / total_dinucleotides) * 100
    non_apobec_percentage = (non_apobec_count / total_dinucleotides) * 100
    return apobec_count, non_apobec_count, total_bases, apobec_percentage, non_apobec_percentage

def create_apobec_partition(sequences):
    """Create APOBEC3 partition."""
    seq_length = len(sequences[0])
    apobec_sites = set()
    valid_bases = set('ATCG')

    # Identify APOBEC sites
    for i in range(seq_length - 1):
        if any(seq[i:i+2] in ['GA', 'TC'] for seq in sequences):
            apobec_sites.add(i)
            apobec_sites.add(i+1)

    # Create initial APOBEC partition
    apobec_partition = [['N'] * seq_length for _ in sequences]
    for i, seq in enumerate(sequences):
        for j in apobec_sites:
            apobec_partition[i][j] = seq[j] if seq[j] in valid_bases else 'N'

    # Mask positions that are always A or T
    for i in range(seq_length):
        if i not in apobec_sites:
            continue
        bases = set(seq[i] for seq in sequences if seq[i] in valid_bases)
        if bases.issubset({'A', 'T'}):
            for seq in apobec_partition:
                seq[i] = 'N'

    # Convert lists to strings
    apobec_partition = [''.join(seq) for seq in apobec_partition]

    return apobec_partition, apobec_sites

def create_non_apobec_partition(sequences, apobec_partition):
    """Create non-APOBEC3 partition by reversing the APOBEC partition logic."""
    valid_bases = set('ATCG')
    non_apobec_partition = []

    for seq, apobec_seq in zip(sequences, apobec_partition):
        non_apobec_seq = []
        for base, apobec_base in zip(seq, apobec_seq):
            if apobec_base == 'N':
                non_apobec_seq.append(base if base in valid_bases else 'N')
            else:
                non_apobec_seq.append('N')
        non_apobec_partition.append(''.join(non_apobec_seq))

    return non_apobec_partition

def analyze_apobec_sites(sequences):
    """Analyze APOBEC target sites across all sequences."""
    site_data = defaultdict(lambda: {'G': 0, 'A': 0, 'C': 0, 'T': 0})
    seq_length = len(sequences[0])
    
    for i in range(seq_length - 1):
        dinucleotides = [seq[i:i+2] for seq in sequences if seq[i:i+2] not in ['NN', 'N-', '-N', '--']]
        if dinucleotides:
            for dn in dinucleotides:
                if dn[0] in ['G', 'A'] and dn[1] == 'A':  # GA or AA
                    site_data[i+1][dn[0]] += 1  # Add 1 to index
                elif dn == 'TC' or dn == 'TT':  # TC or TT
                    site_data[i+2][dn[1]] += 1  # Add 1 to index, and it's the second base
    
    return site_data

def write_apobec_site_analysis(site_data, output_file):
    """Write APOBEC site analysis to a file with interpretation summary."""
    total_potential_conversions = 0
    total_positions_with_conversions = 0
    
    with open(output_file, 'w') as f:
        f.write("Position\tG\tA\tC\tT\tConverted_APOBEC_Sites\n")
        for pos, counts in sorted(site_data.items()):
            g_count = counts['G']
            a_count = counts['A']
            c_count = counts['C']
            t_count = counts['T']
            converted_sites = min(g_count, a_count) + min(c_count, t_count)
            if converted_sites > 0:
                f.write(f"{pos}\t{g_count}\t{a_count}\t{c_count}\t{t_count}\t{converted_sites}\n")
                total_potential_conversions += converted_sites
                total_positions_with_conversions += 1
        
        # Write summary and interpretation guide
        f.write("\n\nSUMMARY AND INTERPRETATION GUIDE:\n")
        f.write("===================================\n\n")
        f.write(f"Total positions with potential APOBEC conversions: {total_positions_with_conversions}\n")
        f.write(f"Total potential APOBEC conversions: {total_potential_conversions}\n\n")
        f.write("How to interpret this file:\n")
        f.write("1. Each row represents a position in the alignment where there's variation in APOBEC target sites.\n")
        f.write("2. G and C are original APOBEC target bases; A and T are potential conversion products.\n")
        f.write("3. 'Converted_APOBEC_Sites' shows the minimum number of sequences that show a conversion at this position.\n")
        f.write("4. A non-zero value in 'Converted_APOBEC_Sites' indicates that some sequences show a conversion while others don't.\n")
        f.write("5. Example interpretation:\n")
        f.write("   Position  G  A  C  T  Converted_APOBEC_Sites\n")
        f.write("   100       8  2  0  0  2\n")
        f.write("   This means at position 100, 8 sequences have G (from GA), 2 have A (from AA), suggesting 2 potential G to A conversions.\n")
        f.write("\nNote: This analysis excludes ambiguous regions (N or gap characters) in the sequences.\n")

def create_initial_apobec_partition(sequences):
    """Create initial APOBEC3 partition by masking non-APOBEC motifs."""
    apobec_partition = []

    for seq in sequences:
        apobec_seq = list('N' * len(seq))
        for i in range(len(seq) - 1):
            if seq[i:i+2] == 'GA':
                apobec_seq[i] = 'G'
                apobec_seq[i+1] = 'A'
            elif seq[i:i+2] == 'TC':
                apobec_seq[i] = 'T'
                apobec_seq[i+1] = 'C'
        apobec_partition.append(''.join(apobec_seq))

    return apobec_partition

def main():
    # Prompt for input file
    while True:
        input_file = input("Please enter the name of your input FASTA file: ")
        if os.path.isfile(input_file):
            break
        else:
            print(f"Error: File '{input_file}' not found. Please try again.")

    # Read sequences
    records = list(SeqIO.parse(input_file, "fasta"))
    sequences = [str(record.seq) for record in records]

    # Count APOBEC and non-APOBEC motifs
    motif_data = []
    for record in records:
        apobec_count, non_apobec_count, total_bases, apobec_percentage, non_apobec_percentage = count_motifs(str(record.seq))
        motif_data.append((record.id, apobec_count, non_apobec_count, total_bases, apobec_percentage, non_apobec_percentage))

    # Sort the data based on APOBEC_Motif_Count
    motif_data.sort(key=lambda x: x[1])

    # Write sorted data to output file
    output_file = "apobec_motif_counts.txt"
    with open(output_file, 'w') as f:
        f.write("Sequence_ID\tAPOBEC_Motif_Count\tNon_APOBEC_Motif_Count\tTotal_Bases\tAPOBEC_Percentage\tNon_APOBEC_Percentage\n")
        for data in motif_data:
            f.write(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\t{data[4]:.2f}%\t{data[5]:.2f}%\n")

    print(f"Sorted motif counts and percentages written to {output_file}")

    # Analyze APOBEC target sites
    site_data = analyze_apobec_sites(sequences)
    
    # Write APOBEC site analysis to a file
    analysis_file = "Potential_APOBEC_Conversions.txt"
    write_apobec_site_analysis(site_data, analysis_file)
    print(f"APOBEC site analysis written to {analysis_file}")

    # Create APOBEC3 partition
    apobec_partition, apobec_sites = create_apobec_partition(sequences)

    # Write APOBEC partition to file
    base_name = os.path.splitext(input_file)[0]
    apobec_file = f"{base_name}_APOBEC3_partition.fasta"

    with open(apobec_file, 'w') as f:
        for record, seq in zip(records, apobec_partition):
            f.write(f">{record.id}\n{seq}\n")

    print(f"APOBEC partition created: {apobec_file}")

    # Create non-APOBEC3 partition
    non_apobec_partition = create_non_apobec_partition(sequences, apobec_partition)

    # Write partitions to files
    non_apobec_file = f"{base_name}_non_APOBEC3_partition.fasta"

    with open(non_apobec_file, 'w') as f:
        for record, seq in zip(records, non_apobec_partition):
            f.write(f">{record.id}\n{seq}\n")

    print(f"Partitions created: {apobec_file} and {non_apobec_file}")

if __name__ == "__main__":
    main()