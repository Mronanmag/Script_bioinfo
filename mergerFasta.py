#!/usr/bin/env python3

__author__ = "Magouroux Ronan"
__version__ = "1.0.0"
__date__ = "2023-07-21"
__email__ = "ronanmagouroux@free.fr"

import sys
import os
import argparse

def recupererArgument() :
	parser = argparse.ArgumentParser(prog="Merger fasta",
									description="Récupère la liste des fichier fasta dans un dossier et les merges",
									epilog="Pour utiliser le programme veuillez inserer un dossier input et output")
	parser.add_argument('-i','--input',type=str,required=True)
	parser.add_argument('-o','--output',type=str,required=True)
	args = parser.parse_args()
	if not args.input.endswith("/") :
		args.input += "/"
	return args.input,args.output

def fastaFinder(path) :
	fastaList = []
	for file in os.listdir(path) :
		if file.endswith(".fna") or file.endswith(".fasta") or file.endswith(".fa") or file.endswith(".ffn") or file.endswith(".fa") :
			fastaList.append(file)
	return fastaList

def fastaMerger(input_path,path, fastaList) :
	merger = open(path, "w")
	print(fastaList)
	for fasta in fastaList :
		fastaFile = open(input_path + fasta, "r")
		for line in fastaFile :
			merger.write(line)
		fastaFile.close()
	merger.close()


input_path, output_file = recupererArgument()
fastaList = fastaFinder(input_path)
fastaMerger(input_path,output_file, fastaList)
