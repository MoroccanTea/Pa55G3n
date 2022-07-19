from tkinter import *
import Pa55G3n as pg
from PIL import Image, ImageTk


def start():
    root = Tk()
    root.title('pa55G3n V' + str(pg.version))
    mainCanvas = newCanvas(root)

    createToolbar(root)

    # Logo
    logo = Image.open('static/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logoLabel = Label(root, image=logo)
    logoLabel.image = logo
    logoLabel.grid(row=0, column=1)
    root.iconphoto(False, logo)

    # Generate a password Button
    NewPassButton = Button(mainCanvas, text='Generate a password', command=pg.generate())
    NewPassButton.grid(columnspan=3, row=2, column=0)

    # See saved passwords Button
    viewPasswordsButton = Button(mainCanvas, text='View saved passwords', command=pg.showPasswords)
    viewPasswordsButton.grid(columnspan=3, row=3, column=0)

    # Credits
    instructions = Label(root, text='\nPa55G3n V' + str(pg.version) + ' by MoroccanTea\n')
    instructions.grid(columnspan=3, row=1, column=0)

    root.mainloop()


def createGenPassCanvas(root, existingCanvas):
    existingCanvas.destroy()
    canvas = Canvas(root, width=350, height=500)
    canvas.grid(columnspan=3)
    simplePassButton = Radiobutton(root, text='Simple', value='simple')
    simplePassButton.grid(columnspan=3, row=1, column=2)
    mediumPassButton = Radiobutton(root, text='Medium', value='medium')
    mediumPassButton.grid(columnspan=3, row=2, column=2)
    hardPassButton = Radiobutton(root, text='Hard', value='hard')
    hardPassButton.grid(columnspan=3, row=3, column=2)
    securePassButton = Radiobutton(root, text='Secure', value='secure')
    securePassButton.grid(columnspan=3, row=4, column=2)


def newCanvas(root):
    canvas = Canvas(root, width=350, height=500)
    canvas.grid(columnspan=3)
    return canvas


# Toolbar
def createToolbar(root):

    menu = Menu(root)
    root.config(menu=menu)
    subMenu = Menu(menu)
    menu.add('cascade', label='File', menu=subMenu)
    subMenu.add_command(label='Generate', command=pg.passComplexity)
    subMenu.add_command(label='View saved passwords', command=pg.showPasswords)
    subMenu.add_separator()
    subMenu.add_command(label='Exit', command=root.destroy)

    editMenu = Menu(menu)
    menu.add('cascade', label='Edit', menu=editMenu)
    editMenu.add_command(label='Edit passwords')
    editMenu.add_command(label='Settings')

    helpMenu = Menu(menu)
    menu.add('cascade', label='Help', menu=helpMenu)
    helpMenu.add_command(label='Help')
    helpMenu.add_command(label='About')


if __name__ == '__main__':
    start()
