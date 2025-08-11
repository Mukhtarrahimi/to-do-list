import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

# Icon
image_icon = PhotoImage(file="images/task.png")
root.iconphoto(False, image_icon)

# top bar
top_image = PhotoImage(file="images/topbar.png")
Label(root, image=top_image).pack()

dock_image = PhotoImage(file="images/dock.png")
Label(root, image=dock_image).place(x=30, y=25)

note_image = PhotoImage(file="images/task.png")
Label(root, image=note_image).place(x=30, y=25)

root.mainloop()  