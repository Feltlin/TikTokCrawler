from tkinter import *
from tkinter import ttk

def click():
    print("Button clicked.")

def submit():
    text = entry.get()
    print(text)
    entry.config(state = DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

def display():
    if x.get() == 1:
        print("You agree.")
    else:
        print("You don't agree.")

def openFile():
    print("File Opened.")

def saveFile():
    print("File saved.")

def Cut():
    print("Cut.")
def Copy():
    print("Copy.")
def Paste():
    print("Paste.")
    
window = Tk()

window.geometry("800x600")
window.title("Tkinter Test Program")
icon = PhotoImage(file = "./Image/TikTok_Logo.png")
window.iconphoto(True, icon)
window.config(background = "#000000")

photo = PhotoImage(file = "./Image/material-symbols--download-rounded.png")

x = IntVar()

menubar = Menu(window)
window.config(menu = menubar)

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text = "Tab 1")
notebook.add(tab2, text = "Tab 2")
notebook.pack(expand = True, fill = "both")
Label(tab1, text = "Hello Tab 1", width = 50, height = 25).pack()
Label(tab2, text = "Hello Tab 2", width = 50, height = 25).pack()

button = Button(window,
                text = "Click",
                command = click,
                font = ("Comic Sans", 30),
                fg = "#00ff00",
                bg = "black",
                activeforeground = "#00ff00",
                activebackground = "black",
                state = ACTIVE,
                image = photo,
                compound = LEFT
                )
button.pack()

entry = Entry(window,
              font = ("Arial", 20),
              fg = "#00ff00",
              bg = "black",
              show = '*'
              )
entry.insert(0, "Type here")
entry.pack(side = LEFT)

submit_button = Button(window, text = "submit", command = submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window, text = "delete", command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text = "backspace", command = backspace)
backspace_button.pack(side = RIGHT)

check_button = Checkbutton(window,
                           text = "I agree.",
                           variable = x,
                           onvalue = 1,
                           offvalue = 0,
                           command = display
                        )
check_button.pack()

fileMenu = Menu(menubar, tearoff = 0, font = ("MV Boli", 15))
menubar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Open", command = openFile)
fileMenu.add_command(label = "Save", command = saveFile)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = quit)

editMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Cut", command = Cut)
editMenu.add_command(label = "Copy", command = Copy)
editMenu.add_command(label = "Paste", command = Paste)

# label = Label(window,
#               text = "Hello tk",
#               font = ("Arial", 40, 'bold'),
#               fg = "green",
#               bg = "black",
#               relief = RAISED,
#               bd = 10,
#               padx = 20,
#               pady = 20,
#             #   image = photo,
#             #   compound = BOTTOM
#             )
# label.pack()
# # label.place(x = 0, y = 0)

window.mainloop()
