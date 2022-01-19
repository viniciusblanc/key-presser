from tkinter import *
from tkinter import ttk
import time

control = False

def elapsed_time():
    n = 0
    global control
    if control:
        control = False
    else:
        control = True
    while control:
        m, s = divmod(n, 60)
        cronom.set(str('{:02}:{:02}'.format(m, s)))
        time.sleep(1)
        n += 1
        root.update()

root = Tk()
root.title("Cronômetro")

mainframe = ttk.Frame(root, borderwidth=5, relief="ridge", width=200, height=100)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

cronom = StringVar()
ttk.Label(mainframe, textvariable=cronom).grid(column=1, row=1, columnspan=3, rowspan=2, sticky=(N, W, E, S)) # , sticky=(W, E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

ttk.Button(mainframe, text="(Re)Start", command=elapsed_time).grid(column=3, row=3) # , sticky=W

root.mainloop()