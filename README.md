# PDF-Generator

This project is a Python-based PDF certificate generator that automates the process of creating personalized certificates for a list of names. It uses `reportlab` to handle PDF creation and `PyPDF2` for merging generated content with a predefined PDF template.

## Features

- Generates personalized certificates.
- Merges personalized text onto a predefined PDF template.
- Outputs certificates as PDF files in a specified directory.

## Prerequisites

Before you can run this script, you will need Python installed on your system along with the following Python libraries:

- reportlab
- PyPDF2

You can install these with pip:

```bash
pip install reportlab PyPDF2
Usage

To use the PDF-Generator, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/William-Misiaszek/PDF-Generator.git
Navigate to the cloned directory:
bash
Copy code
cd PDF-Generator
Run the script:
bash
Copy code
python PDFGEN.py
The script will generate PDFs and save them to the /OUTPUT directory.

Configuration

Setting Your Own Template
To use your own PDF template:

Place your PDF template file into the project directory.
Modify the template_pdf_path in the PDFGEN.py script to point to your template file. For example:
python
Copy code
template_pdf_path = '/path/to/your/template.pdf'
Customizing Names
You can customize the names by modifying the names list in PDFGEN.py.

Example of names list:

python
Copy code
names = [
    ("First", "Last"),
    ("Jane", "Doe")
]
Contributing

Contributions are welcome! If you have improvements or bug fixes:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License


Thank you for checking out the PDF-Generator!
