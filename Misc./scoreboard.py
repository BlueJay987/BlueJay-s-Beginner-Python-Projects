import tkinter as tk
import tkinter.ttk as ttk

#abrieviations
#scr = score
#ct = count

#var
global scr1
global scr2

scr1 = 0
scr2 = 0

#functions

def add1():
    global scr1
    scr1 = scr1 + 1
    scrct1.delete(0, tk.END)
    scrct1.insert(0, str(scr1)
)

def sub1():
    global scr1
    scr1 = scr1 - 1
    scrct1.delete(0, tk.END)
    scrct1.insert(0, str(scr1)
)

def add2():
    global scr2
    scr2 = scr2 + 1
    scrct2.delete(0, tk.END)
    scrct2.insert(0, str(scr2)
)

def sub2():
    global scr2
    scr2 = scr2 - 1
    scrct2.delete(0, tk.END)
    scrct2.insert(0, str(scr2)
)

def reset():
    scr1 = 0
    scr2 = 0
    scrct2.delete(0, tk.END)
    scrct2.insert(0, str(scr2))
    scrct1.delete(0, tk.END)
    scrct1.insert(0, str(scr1))

    

    
#create bases
window = tk.Tk()
window.configure(bg="#282828")

frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame.pack()

frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=0)
frame2.pack()
frame2.configure(bg="#282828")

title = tk.Label(
    text="Scoreboard",
    bg="#282828",
    fg="white",
    master=frame2
)

#scr 1

addbutton1 = tk.Button(
    text="+",
    width=3,
    height=2,
    bg="#000000",
    fg="white",
    relief="solid",
    cursor="hand2",
    command=add1,
    
)
scrct1 = tk.Entry(
    justify="center",
    background="#ff0000",
    width=7
)
subtractbutton1 = tk.Button(
    text="-",
    width=3,
    height=2,
    bg="#000000",
    fg="white",
    relief="solid",
    cursor="hand2",
    command=sub1
)

#scr 2

addbutton2 = tk.Button(
    text="+",
    width=3,
    height=2,
    bg="#000000",
    fg="white",
    relief="solid",
    cursor="hand2",
    command=add2
    
)
scrct2 = tk.Entry(
    justify="center",
    background="#00ff00",
    width=7
)
subtractbutton2 = tk.Button(
    text="-",
    width=3,
    height=2,
    bg="#000000",
    fg="white",
    relief="solid",
    cursor="hand2",
    command=sub2
)

resetbutton = tk.Button(
    text="Reset",
    width=3,
    height=2,
    bg="#000000",
    fg="white",
    relief="solid",
    cursor="hand2",
    command=reset,
    master=frame2,
)

title.pack(fill=tk.BOTH, side=tk.TOP, expand=False, padx=5, pady=10)

addbutton1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

scrct1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

subtractbutton1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

addbutton2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

scrct2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

subtractbutton2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

resetbutton.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=10, pady=10)

window.mainloop()