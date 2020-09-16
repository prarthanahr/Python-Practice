import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('xxx.pdf')
    print("donwwww")
