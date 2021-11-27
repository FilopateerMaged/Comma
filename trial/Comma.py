import tkinter as tk

import os

import re


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


def comma():
    text_box2.delete("1.0", tk.END)
    str = text_box.get("1.0", tk.END)
    lst = str.split(" ")
    print(lst)
    lst2 = []
    rez = []
    rez2 = []
    for x in lst:
        if x != "":
            lst2.append(x)
    for x in lst2:
        print(x)
    print(lst2)
    # for x in lst2:
    #     x.replace("\n", ",")
    #     rez.append(x.lstrip("\n"))
    # print(rez)

    str = ",".join(lst)
    print(str)
    addToClipBoard(str.rstrip(","))
    text_box2.insert("1.0", str.rstrip(","))


window = tk.Tk()
window.title("Comma 1.5")
window.iconbitmap(r'C:\Projects\comma\comma.ico')
w = tk.Label(window, text="Paste Orchestre Devices Below")
w.pack()
text_box = tk.Text()
text_box.pack()
text_box2 = tk.Text()
text_box2.pack()
button = tk.Button(
    text="COPY AND FORMAT",
    width=90,
    height=5,
    bg="orange",
    fg="black",
    command=comma,
)
button.pack()
window.mainloop()
