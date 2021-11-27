import tkinter as tk

import os

import re


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


def comma():
    text_box2.delete("1.0", tk.END)
    str = text_box.get("1.0", tk.END)
    lst = str.split("\n")
    print(lst)
    lst2 = []
    rez2 = []
    for x in lst:
        lst2.append(x.replace(" ", ","))
    str = ",".join(lst2)
    lst3 = str.split(",")
    print(lst3)
    for x in lst3:
        if x != "," and x != "":
            rez2.append(x)
    print(rez2)
    str = ",".join(rez2)
    print(str)
    addToClipBoard(str.rstrip(","))
    text_box2.insert("1.0", str.rstrip(","))


window = tk.Tk()
window.title("Comma 2.0")
w = tk.Label(window, text="Paste Orchestre Devices Below")
w.pack()
text_box = tk.Text(height=20)
text_box.pack()
text_box2 = tk.Text(height=10)
text_box2.pack()
button = tk.Button(
    text="FORMAT AND COPY",
    width=92,
    height=5,
    bg="orange",
    fg="black",
    command=comma,
)
button.pack()
window.mainloop()
