import PyPDF2

fileName = 'pdf.pdf'
# Open the PDF file.
pdf_file = open(fileName, 'rb')

# Create a reader object for the PDF file.
reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file.
num_pages = len(reader.pages)
# Extract the text from the first page of the PDF file.

for i in range(num_pages):
    print(reader.pages[i].extract_text())