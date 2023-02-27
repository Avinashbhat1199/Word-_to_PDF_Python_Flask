import workbook


workbook = Workbook("Book1.xlsx")

# Convert Excel to PDF
workbook.save("xlsx-to-pdf.pdf", SaveFormat.PDF)