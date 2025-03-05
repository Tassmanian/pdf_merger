import os
from PyPDF2 import PdfMerger

def merge_pdfs(file_paths, output_path):
    merger = PdfMerger()

    for path in file_paths:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue

        with open(path, 'rb') as file:
            merger.append(file)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f"PDFs merged successfully into {output_path}")
