from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from PyPDF2 import PdfWriter, PdfReader
import io
import os
import csv

# Register the custom TTF font
pdfmetrics.registerFont(TTFont("CustomFont", 'Aphrodite-Slim-Pro.ttf'))

# TEMPLATE UPDATE HERE. Use Relative Path.
# Now, just run it via python3 pdfgen.py
template_pdf_path = 'CIA Citation-FINAL.pdf'

# Output directory
output_dir = 'OUTPUT'

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def read_names_from_csv(csv_filepath):
    names = []
    print(f"Reading names from {csv_filepath}")
    
    with open(csv_filepath, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skip the header if there is one
        next(csvreader, None)
        
        for row in csvreader:
            if row and row[0].strip():  # Ensure the row is not empty and the name is not an empty string
                full_name = row[0].strip()
                names.append(full_name)
                print(f"Added name: {full_name}")
                
    return names

def create_filled_pdf(full_name, font_name, font_size, centered_x, y):
    print(f"Creating filled PDF for {full_name}")
    packet = io.BytesIO()
    
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont(font_name, font_size)

    # Calculate the width of the full name and position it centered
    text_width = stringWidth(full_name, font_name, font_size)
    
    # Calculate the starting X position to center the text
    start_x = centered_x - (text_width / 2)

    # Draw the full name centered
    can.drawString(start_x, y, full_name)
    can.save()
    
    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf

def merge_pdfs(template, new_pdf):
    print("Merging PDFs")
    output = PdfWriter()
    template_page = template.pages[0]
    template_page.merge_page(new_pdf.pages[0])
    output.add_page(template_page)
    return output

def main():
    # Path to your CSV file
    csv_filepath = 'names.csv'
    
    # Check if the file exists
    if not os.path.exists(csv_filepath):
        print(f"CSV file not found: {csv_filepath}")
        return
    
    # Read names from the CSV file
    names = read_names_from_csv(csv_filepath)

    # Centering configuration
    centered_x = 396  # This is Landscape Mode Centered.
    font_size = 27
    font_name = "CustomFont"

    for full_name in names:
        # Reload your existing PDF template for each iteration
        template_pdf = PdfReader(template_pdf_path)
        
        # Create a new PDF with the name filled in
        new_pdf = create_filled_pdf(full_name, font_name, font_size, centered_x, 290)  # Adjust y as needed
        
        # Merge the new PDF with the template
        output_pdf = merge_pdfs(template_pdf, new_pdf)
        
        # Output file path
        output_filepath = os.path.join(output_dir, f"{full_name.replace(' ', '_')}.pdf")
        print(f"Saving certificate for {full_name} as {output_filepath}")
        
        # Save the certificate PDF in the output directory
        with open(output_filepath, "wb") as outputStream:
            output_pdf.write(outputStream)

    print("All certificates have been created.")

if __name__ == "__main__":
    main()
