from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

items = ["toy", "pen", "glue", 'book', "notepad"]
list_of_items = Label(root)
your_item = Label(root)

def pick():
    randomNum = random.randint(0, 4)
    list_of_items["text"] = str(items)
    your_item["text"] = "Your Item Is the: " + str(randomNum)
    
btn = Button(root, text="Choose", command=pick)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
list_of_items.place(relx=0.5, rely=0.5, anchor=CENTER)
your_item.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()