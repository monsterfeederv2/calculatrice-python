import tkinter as tk

root = tk.Tk()


# specify size of window.
root.geometry("1000x800")

T1 = tk.Text(root, height = 5, width = 52)
T2 = tk.Text(root, height = 5, width = 52)
T3 = tk.Text(root, height = 5, width = 52)
demande1 = """Nombre 1"""
demande2 = "opération"
demande3 = "Nombre 2"

l1 = tk.Label(root, text = demande1)
l2 = tk.Label(root, text = demande2)
l3 = tk.Label(root, text = demande3)
l1.config(font =("Courier", 14))
l2.config(font =("Courier", 14))
l3.config(font =("Courier", 14))




b1 = tk.Button(root, text = "Calculer")


b2 = tk.Button(root, text = "Exit",
            command = root.destroy)

l1.pack()
T1.pack()
l2.pack()
T2.pack()
l3.pack()
T3.pack()
b1.pack()
b2.pack()

tk.mainloop()