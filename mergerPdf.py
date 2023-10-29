#!/usr/bin/env python3

__author__ = "Magouroux Ronan"
__version__ = "1.0.0"
__date__ = "2023-07-21"
__email__ = "ronanmagouroux@free.fr"

import argparse 
import os
from pypdf import PdfMerger
import pdfplumber
import pandas as pd



def recupererArgument() :
	parser = argparse.ArgumentParser(prog="Convertisseur PDF vers Excel",
									description="Programme pour convertir des fichiers PDF en Excel",
									epilog="Pour utiliser le programme veuillez inserer un dossier avec les pdfs ")
	parser.add_argument('-i','--input',type=str,required=True)
	args = parser.parse_args()
	if not args.input.endswith("/") :
		args.input += "/"

	return args.input



def listFile(input_path) :
	pdf_files = [file for file in os.listdir(input_path) if file.endswith(".pdf")]
	pdf_files.sort()
	return pdf_files

def mergerPdf(pdf_files,input_path) :
	merger = PdfMerger()
	for pdf in pdf_files :
		merger.append(input_path + pdf)
	merger.write(input_path + "result.pdf")
	print("Les fichiers ont été fusionnés")
	merger.close()


def main() :
	input_path = recupererArgument()
	list_file = listFile(input_path)
	mergerPdf(list_file,input_path)



if __name__ == "__main__" :
	main()
