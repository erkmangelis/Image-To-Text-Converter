import pytesseract
from PIL import Image
from os import walk
from fpdf import FPDF
import os


def main():

    folder = input("Enter the folder that contains images: ")
    folderPath = os.path.expanduser('~')+f"\Desktop\{folder}"

    images = getImageNames(folderPath)

    pdf=FPDF()
    pdf.add_font('sysfont', '', r"c:\WINDOWS\Fonts\times.ttf", uni=True)
    pdf.set_font('sysfont', '',10)
    pdf.set_margins(45, 5, 5)

    for image in images:
        print("Converting to Text...")
        loc = folderPath+ "\\" + image
        text = convertImageToText(loc)

        pdf.add_page()

        for txt in text.split('\n'):
            pdf.write(20, txt)
            pdf.ln(5)

    pdf.output(os.path.expanduser('~')+"\Desktop\Output.pdf", 'F')
    print("Convertion Completed")


def getImageNames(folderPath):

    images = []

    for (dirpath, dirnames, filenames) in walk(folderPath):
        images.extend(filenames)
        break

    return images


def convertImageToText(imageLoc):

    image = Image.open(imageLoc)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    convertedText = pytesseract.image_to_string(image)
    cleanText = convertedText.strip()
    
    return cleanText


if __name__ == "__main__":
    main()