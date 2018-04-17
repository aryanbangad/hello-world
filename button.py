import tkinter as tk

def print_slogan():
	print("a working button")
def quit_print():
	print("bye")
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

slogan = tk.Button(frame,
                   text = "click"
				   ,fg="red",
				   command=print_slogan())

slogan.pack(side = tk.LEFT)

quitbutton = tk.Button(frame,
                       text = "quit",
					   fg="green",
					   command=quit_print())
quitbutton.pack(side = tk.RIGHT)
root.mainloop()