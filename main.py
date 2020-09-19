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
Label(window, image=img).pack()

# slider label
slider_label = Label(
    text="V-Bucks",
    font=("Impact", 12),
    bg="royal blue",

)
slider_label.place(x=16, y=414)

# slider knob
slider_value = IntVar()
slider = Scale(
    window,
    from_=1000, to=100000,
    resolution=1000,
    orient=HORIZONTAL,
    variable=slider_value,
    bg="royal blue",
    width=50,
    length=350,
    font=("Arial Black", 14)
)

slider.place(x=75, y=410)


def display_key():
    """
    on click, display the key
    """

    # generate the codes
    first4 = secrets.token_hex(2)
    second4 = secrets.token_hex(2)
    third4 = secrets.token_hex(2)
    fourth4 = secrets.token_hex(2)

    # display the and label and generated key text
    key_label = Label(
        text=("The Code for " + str(slider_value.get()) + " V-Bucks is"),
        font=("Arial Black", 12),
        bg="grey79",


        )
    key_label.place(x=90, y=330)

    # key text
    key_text = Text(
        window,
        height=1,
        width=21,
        borderwidth=2,
        font=("Impact", 22),
        bg="grey79",

    )
    key_text.insert(1.0, (" " + first4 + " - " + second4 + " - " + third4 + " - " + fourth4))
    key_text.place(x=85, y=360)


# button
genkey_btn = Button(window, text="Generate a Key", command=display_key, bg="PaleGreen2", font=("Impact", 14))
genkey_btn.place(x=175, y=500)


window.mainloop()



