from tkinter import *
from tkinter import messagebox
import requests

app = Tk()
app.geometry('500x250')

# function
def download_image():
    if url_entry.get() == '' or file_entry.get() == '':
        messagebox.showerror('Empty Enties', 'Entry box cannot be empty..')
        return
    url = url_entry.get()
    png_name = file_entry.get() + '.png'

    res = requests.get(url)
    with open(png_name, 'wb') as f:
        f.write(res.content)

# image url
url_label = Label(app,text='Image Url', font=('bold', 15))
url_label.grid(row=0, column=0, padx=20, pady=20)
url_entry = Entry(app, font=('bold', 14), width=30)
url_entry.grid(row=0, column=1)

# file name
file_label = Label(app,text='File Name', font=('bold', 15))
file_label.grid(row=1, column=0, padx=20)
file_entry = Entry(app, font=('bold', 14), width=30)
file_entry.grid(row=1, column=1)

# create image button
create_btn = Button(app, text='Download Image', font=('bold', 12), command=download_image)
create_btn.grid(row=2,column=0, columnspan=2, pady=15)

app.resizable(False, False)
app.mainloop()
