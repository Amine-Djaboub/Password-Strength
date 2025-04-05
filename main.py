
import PIL.Image
import PIL.ImageTk
import re
from tkinter import *

def pressButton():
    password,confirmPassword=getText()
    result=passwordChecker(password,confirmPassword)
    if result == True:
        result_label.config(text="User made Successfully",fg="green")     
    else:
        result_label.config(text=result,fg="red")

def getText():
    password=passwordEntry.get()
    confirmPassword=confirmPasswordEntry.get()
    return password,confirmPassword

def passwordChecker(password: str, confirmPassword: str) -> bool:
    if password == confirmPassword:
        if len(password) < 8:
            return "Password must be at least 8 characters long."
        
        if not any(char.islower() for char in password):
            return "Password must contain at least one lowercase letter."

        if not any(char.isupper() for char in password):
            return "Password must contain at least one uppercase letter."

        if sum(char.isdigit() for char in password) < 2:
            return "Password must contain at least two numbers."

        if not re.search(r"[^\w\s]", password):  # Checks for a non-letter, non-number symbol
            return "Password must contain at least one special character."

        return True
    else:
        return "Password Confirmation Mismatch"
    

root = Tk()
root.geometry("400x300")
root.title('New User')

frame=Frame(root)
frame.pack(expand=True)

# Image fixing

image = PIL.Image.open("pfp.png")
image = image.resize((100, 100))
photo = PIL.ImageTk.PhotoImage(image)

transparent_image = PIL.Image.new("RGBA", image.size, (0, 0, 0, 0))
transparent_image.paste(image, (0, 0), image)

photo = PIL.ImageTk.PhotoImage(transparent_image) 

# End image fixing

image_label = Label(frame, image=photo, bg="#f2f2f2")
image_label.pack()

usernameLable= Label(frame, text='Username: ')
usernameLable.pack()
usernameEntry = Entry(frame)
usernameEntry.pack()

passwordLable= Label(frame, text='Password: ')
passwordLable.pack()
passwordEntry = Entry(frame,show="*")
passwordEntry.pack()

confirmPasswordLable= Label(frame, text='Confirm Password: ')
confirmPasswordLable.pack()
confirmPasswordEntry = Entry(frame,show="*")
confirmPasswordEntry.pack()

result_label = Label(frame, text="",)
result_label.pack()

EmptyLable= Label(frame, text='   ')
EmptyLable.pack()

button = Button(frame, text="New User", command=pressButton)
button.pack()


mainloop()



