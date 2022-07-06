# Text-From-Screenshots
I often like screenshotting certain texts that I find interesting or insightful, particularly tweets. The issue that I encounter, however, is 
that images aren't the best file format to review the compiled content. They take up a lot of memory, can't be easily printed, the text in them can't be 
copied and pasted or modified, etc. The ideal scenario would be to have all of the content in a text file, as it overcomes all of the problems stated 
above, but having to transcribe the content is obviously time-consuming. This is where OCR, concretely the Python module `pytesseract` proves to be very 
useful.

This is a simple script that I wrote to "transcribe" the text in the screenshots into a text file. To make it work, install the relevant modules, 
set the values of `folder_pathname` and `textfile_pathname` to the pathname of the folder in which the screenshots are located and of the blank text file
in which you want the text to be stored, respectively. The gist of the script is that it iterates over the files in the folder, inputs them into the 
`image_to_string` function and adds the text obtained to the text file. In the text files, the tweets are numbered and a string informing of the progress 
is output.

