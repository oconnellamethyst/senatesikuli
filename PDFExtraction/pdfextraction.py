# importing required modules
import pdftotext
import glob
import re


def pdfextraction():
    """
    Program creates text files for each PDF in a folder CourseMaterials (not included)
    in another folder called Materials (not included)
    
    Modifyed excerpt for use of PyPDF2 from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
    and StackOverflow for use of Glob https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
    and Introduction to Computer Science using Python, page 294
    and this https://programminghistorian.org/lessons/working-with-text-files
    and this https://github.com/jalan/pdftotext
    and this https://stackoverflow.com/questions/41668092/return-the-content-of-a-wildcard-match-in-python
    """

    
    name = ''
    
    for filename in glob.glob('CourseMaterials/*.pdf'):
    
        name = re.search('CourseMaterials/(.*).pdf', filename).group(1)
        
        # creating a pdf file object
        with open(filename, 'rb') as pdfFileObj:
            pdfReader = pdftotext.PDF(pdfFileObj)
 
        # number of pages in pdf file
        numPages = len(pdfReader)
    
        for page in pdfReader:
            file = open('Materials/' + str(name) + '.txt','a')
    
            for line in page:
                file.write(line)
            
            file.close()
    return

#Main

pdfextraction()


