from fpdf import FPDF

'''
Documentation: http://www.fpdf.org/
'''

# save FPDF Class in variable
pdf = FPDF()

# add a page
pdf.add_page()

# set style and font size
# pdf.set_font("Arial", size=15)
pdf.set_font("Arial", size=10)

# create cell
# pdf.cell(200, 10, txt="Test test test", ln=2, align='C')
# pdf.cell(200, 10, txt="This is line three", ln=3, align='C')

# open text file in read mode
file = open("test.txt", "r")

# insert text in pdf
for text in file:
  pdf.cell(200, 10, txt=text, ln=1, align='C')

# pdf.output("manualtest.pdf")
pdf.output("test.pdf")