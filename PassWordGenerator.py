import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = ''.join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


window = Tk()
window.title("My pass word Generator")
window.geometry("720x480")
window.iconbitmap("R.ico")
window.config(background='#dee5dc')

# create the principal frame
frame = Frame(window, bg='#dee5dc')

# create image
width = 300
height = 300
image = PhotoImage(file="lock.png").zoom(10).subsample(30)
canvas = Canvas(frame, width=width, height=height, bg='#dee5dc', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#dee5dc')

#
label_title = Label(right_frame, text='Pass word', font=('Helvetica', 20), bg='#dee5dc', fg='black')
label_title.pack()

password_entry = Entry(right_frame, font=('Helvetica', 20), bg='#dee5dc', fg='black')
password_entry.pack()

generate_password_button = Button(right_frame, text='Generate', font=('Helvetica', 20), bg='#dee5dc', fg='black', command=generate_password)
generate_password_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

# centralise frame
frame.pack(expand=YES)


window.mainloop()
