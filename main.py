import tkinter as tk

root = tk.Tk()
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="Hello World!").grid(column=0, row=0)
tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()