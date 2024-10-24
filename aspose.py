import aspose.pdf as ap

# Define the input PDF and output DOCX file paths
pdf_path = "input_files/input.pdf"
docx_path = "output_files/output.docx"

# Load the PDF document
pdf_document = ap.Document(pdf_path)

# Save the PDF as DOCX
pdf_document.save(docx_path, ap.SaveFormat.DOC_X)

print(f"Conversion complete: {docx_path}")
