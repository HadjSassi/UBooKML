from docx import Document


def docx_to_dict(file_name):
    docx_dict = {}
    document = Document(file_name)
    indx = 0
    for para in document.paragraphs:
        indx += 1
        if (len(para.text) > 0):
            docx_dict[indx] = para.text
    return docx_dict

def texting(doc):
    df = docx_to_dict(doc)
    txt = ""
    for pp in df.values():
        txt += pp+"\n"
    return txt

print(texting('2.docx'))