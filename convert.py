from fpdf import FPDF

'''
Documentation: http://www.fpdf.org/
'''

# save FPDF Class in variable
pdf = FPDF()

# add a page
pdf.add_page()

# set style and font size
pdf.set_font("Arial", size=15)

# create cell
pdf.cell(200, 10, txt="Test test test", ln=2, align='C')

pdf.output("manualtest.pdf")