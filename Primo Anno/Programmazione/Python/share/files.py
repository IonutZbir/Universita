import os
from tkinter import filedialog

f = open('prova.txt', 'a')
#\cnae\fdbhb\vsdnbjab\text[0]   .txt[1]
path = os.getcwd()
#folder = os.listdir(filedialog.askdirectory())
#print(folder)

inputPath = filedialog.askdirectory()
listaFile = []
folder = os.listdir(inputPath)
for file in folder:
    pathName = os.path.join(inputPath, file)
    if os.path.splitext(pathName)[1] in ['.txt', '.pdf', '.exe', '.lnk']:
        listaFile.append(pathName)

k = 0
for x in listaFile:
    f.write(str(k + 1) + ". "  + str(x) + "\n")
    k += 1
f.close()
