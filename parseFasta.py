#!/usr/bin/python3

import argparse
from Bio import SeqIO

def parse_fasta_with_biopython(input_file, output_file, query):
    headers = []
    for record in SeqIO.parse(input_file, "fasta"):
        if query in record.description:
            headers.append(record)
    SeqIO.write(headers, output_file, "fasta")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter FASTA file based on query in header.')
    parser.add_argument('-i', '--input', help='Input FASTA file', required=True)
    parser.add_argument('-o', '--output', help='Output FASTA file', required=True)
    parser.add_argument('-q', '--query', help='Query string to search in headers', required=True)
    args = parser.parse_args()

    parse_fasta_with_biopython(args.input, args.output, args.query)
