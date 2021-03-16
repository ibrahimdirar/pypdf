#!/usr/bin/python3

# libraries to import
import tkinter as tk
from tkinter import filedialog
import PyPDF2


def main():

    # creates Tk window
    root = tk.Tk()
    root.update()
    root.withdraw()

    # while True:
    #     try:
    #         number_to_rotate = int(
    #             input('How may pages to rotate? (0 for all): '))
    #     except ValueError:
    #         print("Please type in a number")
    #         continue
    #     else:
    #         while True:
    #             rotate_individually = input(
    #                 'Rotate pages individually? (y/n)')
    #             if(rotate_individually == 'y'):
    #                 while True:
    #                     print('Example: "1, 3, 5-7"')
    #                     page_selection = input('Select pages to rotate:')
    #             elif (rotate_individually == 'n'):
    #                 break
    #             else:
    #                 print("Please type in 'y' or 'n'.")
    #                 continue
    #         break

    # PDFROTATE
    pdf_in = open(filedialog.askopenfilename(), 'rb')
    root.withdraw()
    root.update()
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum % 2:
            page.rotateClockwise(180)
        # else:
        #     page.rotateClockwise(90)
        pdf_writer.addPage(page)

    userfilename = filedialog.asksaveasfilename()

    pdf_out = open(userfilename + '.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()

    # PDFMERGE
    # # asks users where the PDFs are
    # for x in range(number_to_merge):
    #     pdf_to_merge = filedialog.askopenfilename()
    #     root.withdraw()
    #     root.update()
    #     pdf2merge.append(pdf_to_merge)
    #
    # # Ask user for the name to save the file as
    # userfilename = filedialog.asksaveasfilename()
    #
    # # loop through all PDFs
    # for filename in pdf2merge:
    #     # rb for read binary
    #     pdfFileObj = open(filename, 'rb')
    #     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #     # Opening each page of the PDF
    #     for pageNum in range(pdfReader.numPages):
    #         pageObj = pdfReader.getPage(pageNum)
    #         pdfWriter.addPage(pageObj)
    # # save PDF to file, wb for write binary
    # pdfOutput = open(userfilename + '.pdf', 'wb')
    # # Outputting the PDF
    # pdfWriter.write(pdfOutput)
    # # Closing the PDF writer
    # pdfOutput.close()
    # # closes Tk window
    # root.destroy()
    #
    # print('Finished')
