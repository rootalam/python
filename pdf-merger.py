#pip install pypdf
# pip install pycryptodome


from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["ANIRBAN_CSE_2021.pdf", "challan.pdf", "project-owners.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
