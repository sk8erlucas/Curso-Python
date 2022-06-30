import tkinter

def reset():
    opcion.set(None)

window = tkinter.Tk()

opcion = tkinter.IntVar()
opcion.set(None)

radio1 = tkinter.Radiobutton(window, text="Opcion 1", variable=opcion, value=1)
radio1.pack()
radio2 = tkinter.Radiobutton(window, text="Opcion 2", variable=opcion, value=2)
radio2.pack()
radio3 = tkinter.Radiobutton(window, text="Opcion 3", variable=opcion, value=3)
radio3.pack()
radio4 = tkinter.Radiobutton(window, text="Opcion 4", variable=opcion, value=4)
radio4.pack()
radio5 = tkinter.Radiobutton(window, text="Opcion 5", variable=opcion, value=5)
radio5.pack()

tkinter.Button(window, text="Reiniciar", command=reset).pack()

window.mainloop()