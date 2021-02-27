import tkinter as tk

import client

root = tk.Tk()

root.geometry("600x400")


def go():
    """Update target values on server."""
    x = Xvar.get()
    y = Yvar.get()
    z = Zvar.get()
    a = Avar.get()
    b = Bvar.get()
    client.send({"x": x, "y": y, "z": z, "a": a, "b": b})


# Axis Value tkinter Variables
Xvar = tk.DoubleVar(value=0)
Yvar = tk.DoubleVar(value=0)
Zvar = tk.DoubleVar(value=0)
Zvar = tk.DoubleVar(value=0)
Avar = tk.DoubleVar(value=0)
Bvar = tk.DoubleVar(value=0)

# Axis Labels
Xlabel = tk.Label(root, text="X Axis 0-50", font=("calibre", 10, "bold"))
Ylabel = tk.Label(root, text="Y Axis 0-50", font=("calibre", 10, "bold"))
Zlabel = tk.Label(root, text="Z axis 0-50", font=("calibre", 10, "bold"))
Alabel = tk.Label(root, text="A axis 0-50", font=("calibre", 10, "bold"))
Blabel = tk.Label(root, text="B axis 0-50", font=("calibre", 10, "bold"))

# Axis Value Entry Widget
Xentry = tk.Entry(root, textvariable=Xvar, font=("calibre", 10, "normal"))
Yentry = tk.Entry(root, textvariable=Yvar, font=("calibre", 10, "normal"))
Zentry = tk.Entry(root, textvariable=Zvar, font=("calibre", 10, "normal"))
Aentry = tk.Entry(root, textvariable=Avar, font=("calibre", 10, "normal"))
Bentry = tk.Entry(root, textvariable=Bvar, font=("calibre", 10, "normal"))

# Button Widget
GObtn = tk.Button(root, text="Update", command=go)

# Positions of Widgets
Xlabel.grid(row=0, column=0)
Xentry.grid(row=0, column=1)

Ylabel.grid(row=1, column=0)
Yentry.grid(row=1, column=1)

Zlabel.grid(row=2, column=0)
Zentry.grid(row=2, column=1)

Alabel.grid(row=3, column=0)
Aentry.grid(row=3, column=1)

Blabel.grid(row=4, column=0)
Bentry.grid(row=4, column=1)

GObtn.grid(row=5, column=1)


root.mainloop()
