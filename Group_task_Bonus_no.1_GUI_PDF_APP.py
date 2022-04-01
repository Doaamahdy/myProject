from tkinter import *
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

root = Tk()
root.title("pdf manipulator")
root.configure(bg="purple")



def merge():

    mergeFile = PyPDF2.PdfFileMerger()
    mergeFile.append(PyPDF2.PdfFileReader(e.get(), 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader(b.get(), 'rb'))
    mergeFile.write('bor3y.pdf')

def extract():

    file_base_name = d.get().replace(".pdf", "")
    pdf = PdfFileReader(d.get())
    pages = []
    for page in c.get():
        pages.append(int(page))

    pdfWriter = PdfFileWriter()
    for nom in pages:
        pdfWriter.addPage(pdf.getPage(nom))
    with open("{0}_subset.pdf".format(file_base_name), "wb") as f:
        pdfWriter.write(f)
        f.close()

def split_pages():



	pdf = PdfFileReader(f.get())
	for page in range(pdf.getNumPages()):
	    pdf_writer = PdfFileWriter()
	    current_page = pdf.getPage(page)
	    pdf_writer.addPage(current_page)
	    outputFilename = "example-page-{}.pdf".format(page + 1)
	    with open(outputFilename, "wb") as out:
	    	pdf_writer.write(out)
	    	print("created", outputFilename)

root.geometry("400x290")

label1=Label(root,text="Enter the first path pdf:",fg="yellow")
label1.config(bg="purple")
label1.pack()

e = Entry(root, width=50)
e.pack()


label2=Label(root,text="Enter the second pdf path:",fg="yellow")
label2.config(bg="purple")
label2.pack()
b = Entry(root, width=50)
b.pack()




myButton1 = Button(root, text="merge", command=merge)
myButton1.pack()


label3=Label(root,text="Enter the path pdf:",fg="yellow",)
label3.config(bg="purple")
label3.pack()

d = Entry(root, width=50)
d.pack()


label4=Label(root,text="Enter the page to be extracted:",fg="yellow")
label4.config(bg="purple")
label4.pack()

c = Entry(root, width=50)
c.pack()


myButton2 = Button(root, text="extract", command=extract)
myButton2.pack()


label5=Label(root,text="Enter the path pdf:",fg="yellow")
label5.config(bg="purple")
label5.pack()

f = Entry(root, width=50)
f.pack()

myButton3 = Button(root, text="split pages", command=split_pages)
myButton3.pack()
root.mainloop()