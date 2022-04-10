import PyPDF2

# create pdf file reader object
pdf = PyPDF2.PdfFileReader('../1st DT/Scientific/439.pdf')

# TWO STEPS TO EXTRACT TEXT
# Step1: Grap the Page(s)
txt = ""
for i in range(pdf.numPages):
    page_1_object = pdf.getPage(i)
    page_1_text =   page_1_object.extractText()
    txt += page_1_text+"\n"
print(txt)