# importing required modules 
from pypdf import PdfReader 

def getText(pdf_name):
    # creating a pdf reader object 
    reader = PdfReader('test.pdf')  

    # printing number of pages in pdf file 
    print(len(reader.pages)) 

    # getting a specific page from the pdf file 
    page = reader.pages[0] 

    # extracting text from page 
    text = page.extract_text() 
    return text

if __name__=="__main__":
    print(getText('test.pdf'))