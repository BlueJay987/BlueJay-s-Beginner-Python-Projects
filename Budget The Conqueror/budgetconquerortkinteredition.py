#budgetconquerortkinteredition
import tkinter as tk
import tkinter.ttk as ttk

def gettarget():
    with open("targetdistance.txt") as tarfile:
        global tar_dist
        tar_dist = tarfile.read()
        tar_dist = float(tar_dist)
    
def getcomp():
    with open("compdist.txt") as compfile:
        global comp_dist
        comp_dist = compfile.read()
        comp_dist = float(comp_dist)

def view():
    getcomp()
    gettarget()
    entry.delete(0, tk.END)
    percentage = '{:.2%}'.format(comp_dist/tar_dist)
    entry.insert(0, "---" + percentage + " Completed" + "---")

def add():
    getcomp()
    gettarget()
    add_dist = float(entry.get())
    write_dist = comp_dist + add_dist
    write_dist = str(write_dist)
    addcomp = open("compdist.txt", "w")
    addcomp.write(write_dist)
    entry.delete(0, tk.END)
    entry.insert(0, "Miles Logged!")
    addcomp.close()

def clear():
    entry.delete(0, tk.END)

#create bases
window = tk.Tk()
window.configure(bg="#282828")

frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame.pack()

frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=0)
frame2.pack()
frame2.configure(bg="#282828")

#Create Widgets
title = tk.Label(
    text="Budget The Conquerer",
    bg="#282828",
    fg="white",
    master=frame2
)

addbutton = tk.Button(
    text="Add",
    width=10,
    height=5,
    bg="#444444",
    fg="white",
    relief="raised",
    cursor="hand2",
    command=add,
)

viewbutton = tk.Button(
    text="View",
    width=10,
    height=5,
    bg="#444444",
    fg="white",
    relief="raised",
    cursor="hand2",
    command=view,
)

clearbutton = tk.Button(
    text="Clear Text",
    width=10,
    height=1,
    bg="#444444",
    fg="white",
    cursor="hand2",
    master=frame2,
    command=clear
)

entry = tk.Entry(
    justify="center",
)

#Pack everything together
title.pack(fill=tk.BOTH, side=tk.TOP, expand=False, padx=5, pady=10)

addbutton.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

entry.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=10)

viewbutton.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

clearbutton.pack(fill=tk.NONE, side=tk.BOTTOM, expand=True, padx=10, pady=10)

window.mainloop()
