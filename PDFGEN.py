from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from PyPDF2 import PdfWriter, PdfReader
import io
import os

# Register the custom TTF font
pdfmetrics.registerFont(TTFont("CustomFont", '/Users/wmisiasz/Documents/CODE/PDFGEN/Aphrodite-Slim-Pro.ttf'))

# List of names to be filled in the certificates
names = [
    ("Bob", "Marley"),
    ("William", "Fancy Pants"),
]


# Your existing PDF file
template_pdf_path = '/Users/wmisiasz/Documents/CODE/PDFGEN/CIA.pdf'

# Output directory
output_dir = '/Users/wmisiasz/Documents/CODE/PDFGEN/OUTPUT'

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

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

# Centering configuration
centered_x = 400  # Adjust this to the center x coordinate of where you want the names
font_size = 27
font_name = "CustomFont"

for first_name, last_name in names:
    # Reload your existing PDF template for each iteration
    template_pdf = PdfReader(template_pdf_path)
    
    # Full name
    full_name = f"{first_name} {last_name}"
    
    # Create a new PDF with the name filled in
    new_pdf = create_filled_pdf(full_name, font_name, font_size, centered_x, 290)  # Adjust y as needed
    
    # Merge the new PDF with the template
    output_pdf = merge_pdfs(template_pdf, new_pdf)
    
    # Output file path
    output_filepath = os.path.join(output_dir, f"{first_name}_{last_name}_certificate.pdf")
    print(f"Saving certificate for {full_name} as {output_filepath}")
    
    # Save the certificate PDF in the output directory
    with open(output_filepath, "wb") as outputStream:
        output_pdf.write(outputStream)

print("All certificates have been created.")
