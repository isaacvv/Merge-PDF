import fitz
import fitz
doc = fitz.open("Test1.pdf")


if doc.isEncrypted:
    print("is encrypted")
    doc.authenticate("test123")

    doc1 = fitz.open()

    doc1.insertPDF(doc)
    
    doc1.save("test123.pdf")

else:
    doc.newPage()