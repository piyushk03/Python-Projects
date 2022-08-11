import pyttsx3
import PyPDF2
book = open('DBMS.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfreader.getPage(7)
txt = page.extract_text()
speaker.say(txt)
speaker.runAndWait()
