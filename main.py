from tkinter import *
from PIL import ImageTk, Image
import secrets


# window config
window = Tk()
window.geometry("500x600")
window.title("Duke KeyGen of Death")
window.configure(background="blue")
window.resizable(False, False)

#  photo stuff
fortnite_img_path = "resources/fortnite.jpg"
img = ImageTk.PhotoImage(Image.open(fortnite_img_path))
Label(window, image=img, bg="black").pack()


# slider knob
value = IntVar()

slider = Scale(
    window,
    from_=100, to=10000,
    resolution=100,
    orient=HORIZONTAL,
    variable=value,
    bg="royal blue",
    width=75,
    length=350,
    font=("Arial Black", 14)
)

slider.place(x=100, y=375)


def display_key():
    """
    on click, display the key
    """

    first4 = secrets.token_hex(2)
    second4 = secrets.token_hex(2)
    third4 = secrets.token_hex(2)
    fourth4 = secrets.token_hex(2)

    key_text = Text(window, height=1, width=21, borderwidth=2, font=("Helvetica", 14))
    key_text.insert(1.0, (" " + first4 + " - " + second4 + " - " + third4 + " - " + fourth4))
    key_text.place(x=125, y=275)
    key_text.configure(state="disabled")


# button
genkey_btn = Button(window, text="Generate a Key", command=display_key, bg="PaleGreen2", font=("Impact", 14))
genkey_btn.place(x=200, y=500)


window.mainloop()



