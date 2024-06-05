from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Set the pagesize to landscape by switching the width and height
landscape_letter = (letter[1], letter[0])

# Create a new PDF with Reportlab in landscape orientation
c = canvas.Canvas("grid_landscape.pdf", pagesize=landscape_letter)

# Draw a grid
for x in range(0, int(landscape_letter[0]), 72): # Width for landscape orientation
    for y in range(0, int(landscape_letter[1]), 72): # Height for landscape orientation
        c.drawString(x, y, f"{x},{y}")
        c.line(x, 0, x, landscape_letter[1])  # Draw vertical lines
        c.line(0, y, landscape_letter[0], y)  # Draw horizontal lines

c.save()
