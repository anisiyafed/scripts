import PyPDF2
import os

def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output_filename, "wb") as output_file:
        pdf_merger.write(output_file)
        print(f"Merged PDF saved as: {output_filename}")

pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

if len(pdf_files) >= 2:
    output_file = "merged_output.pdf"
    merge_pdfs(pdf_files, output_file)
else:
    print("Not enough PDF files found to merge.")
