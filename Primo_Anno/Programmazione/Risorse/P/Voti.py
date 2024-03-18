from tkinter import *
import os

FILENAME = os.path.join(os.getcwd(), "voti.csv")
RESOLUTION = "300x400"
TITLE = "Grades Manager"

root = Tk()
root.geometry(RESOLUTION)
root.title(TITLE)
inputFrame = Frame(root).pack()
btnFrame = Frame(root).pack()


def createBox(frame):
    caselle = {}
    for x in ['Cognome', 'Nome', 'Voto']:
        caselle[x] = {'label': Label(text=x, pady=5, fg='red'), 'text': Text(
            frame, height=1, width=25, pady=5)}
    return caselle

def pop_up(frame):
    top = Toplevel(frame)
    top.geometry("200x100")
    top.title("Errore")
    Label(top, text= f"Casella '{x}' vuota!!", ).pack(ipady=20)

def inputText(inputBox, fileName):
    """
    Return: dizionario -> {'cognome', 'nome', 'voto'}
    """
    text = {}
    #print(inputBox)
    for x in inputBox.keys():
        text[x] = inputBox[x]['text'].get("1.0", "end-1c")
        if text[x] == '':
            pop_up(inputFrame)

    file = open(fileName, "a")
    row = ''
    keys = [*text.keys()]
    for x in keys:
        row += f'{x}: {text[x]} ' if x != keys[-1] else f'{x}: {text[x]}'
    file.write(row + "\n-------------\n")
    file.close()

def deleteVoti(filename):
    file = open(filename, 'w')
    file.write('')
    file.close()
    

caselle = createBox(inputFrame)
#print(caselle)
insertBtn = Button(btnFrame, height = 2,
                   width = 15,
                   text = "Aggiungi",
                   command = lambda: inputText(caselle, FILENAME),
                   cursor = 'hand2',
                   background = "light green",
                   fg = "dark green",
                   font = "Helvetica 10 bold",
                   borderwidth=1)
                   
quitBtn = Button(btnFrame, height = 2,
                 width = 15,
                 text = "Exit",
                 command = root.destroy,
                 cursor = 'hand2',
                 background = "light green",
                 fg = "dark green",
                 font = "Helvetica 10 bold",
                 borderwidth=1)

deleteAllBtn = Button(btnFrame, height = 2,
                 width = 15,
                 text = "Cancella Voti",
                 command = lambda: deleteVoti(FILENAME),
                 cursor = 'hand2',
                 background = "red",
                 fg = "white",
                 font = "Helvetica 10 bold",
                 borderwidth=1)

for x in caselle.values():
    x['label'].pack()
    x['text'].pack()

insertBtn.pack(side=TOP, pady=10)
quitBtn.pack(side=TOP, pady=10)
deleteAllBtn.pack(side=TOP, pady=10)

mainloop()
