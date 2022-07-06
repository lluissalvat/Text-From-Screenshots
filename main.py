import os
import pytesseract
from PIL import Image

folder_pathname = '/Users/lluissalvat/Desktop/TwitterScreenshots'
textfile_pathname = '/Users/lluissalvat/Downloads/prova.txt'

mylist = os.listdir(folder_pathname)

elements = [folder_pathname+'/{0}'.format(element) for element in mylist]

fd = open(textfile_pathname, 'w')

for element in elements:

    value = Image.open(element)
    text = pytesseract.image_to_string(value)

    print('Tweet '+str(elements.index(element)+1),file=fd)
    print(' ', file=fd)
    print(text, file=fd)
    print(' ', file=fd)
    print('Status: '+str(elements.index(element)+1)+'/'+str(len(elements))+' '+str(round((elements.index(element)+1)*100/len(elements),2))+'%')

fd.close()
