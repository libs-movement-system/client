import re
import tkinter as tk

import client

root = tk.Tk()

root.geometry("600x400")


# What the button does
def go():

    x = Xvar.get()
    y = Yvar.get()
    z = Zvar.get()

    x = re.sub("[^0-9.]", "", x)
    y = re.sub("[^0-9.]", "", y)
    z = re.sub("[^0-9.]", "", z)

    Xvar.set(x)
    Yvar.set(y)
    Zvar.set(z)

    data = {"x": float(x), "y": float(y), "z": float(z)}
    client.send(data)


# Axis Value tkinter Variables
Xvar = tk.StringVar()
Yvar = tk.StringVar()
Zvar = tk.StringVar()

# Axis Labels
Xlabel = tk.Label(root, text="X Axis 0-50", font=("calibre", 10, "bold"))
Ylabel = tk.Label(root, text="Y Axis 0-50", font=("calibre", 10, "bold"))
Zlabel = tk.Label(root, text="Z axis 0-50", font=("calibre", 10, "bold"))

# Axis Value Entry Widget
Xentry = tk.Entry(root, textvariable=Xvar, font=("calibre", 10, "normal"))
Yentry = tk.Entry(root, textvariable=Yvar, font=("calibre", 10, "normal"))
Zentry = tk.Entry(root, textvariable=Zvar, font=("calibre", 10, "normal"))

# Button Widget
GObtn = tk.Button(root, text="GO", command=go)

# Positions of Widgets
Xlabel.grid(row=0, column=0)
Xentry.grid(row=0, column=1)
Ylabel.grid(row=1, column=0)
Yentry.grid(row=1, column=1)
Zlabel.grid(row=2, column=0)
Zentry.grid(row=2, column=1)
GObtn.grid(row=3, column=1)


root.mainloop()
