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
root.mainloop()  