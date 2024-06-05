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
```
## Usage

To use the PDF-Generator, follow these steps:

Clone the repository:
```bash
git clone https://github.com/yourusername/PDF-Generator.git
```
Navigate to the cloned directory:
```bash
cd PDF-Generator
```
Run the script:
```bash
python PDFGEN.py
```
The script will generate PDFs and save them to the /OUTPUT directory.

## Configuration

Setting Your Own Template
To use your own PDF template:

Place your PDF template file into the project directory.
Modify the template_pdf_path in the PDFGEN.py script to point to your template file. For example:
```bash
template_pdf_path = '/path/to/your/template.pdf'
```
## Customizing Names
You can customize the names by modifying the names list in PDFGEN.py.

Example of names list:

```bash
git clone https://github.com/yourusername/PDF-Generator.git
cd PDF-Generator
python PDFGEN.py
```
