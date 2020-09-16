from tkinter import *
import secrets
from pygame import mixer

# window config
window = Tk()
window.geometry("447x314")
window.title("Duke KeyGen of Death")
window.configure(background="black")
window.resizable(False, False)

#  photo
skull_photo = PhotoImage(file="skull.gif")
Label(window, image=skull_photo, bg="black").grid(row=0, column=0, sticky=E)

# audio mixer
mixer.init()
mixer.music.load("tune.mp3")
mixer.music.play()


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
genkey_btn = Button(window, text="Generate a Key", command=display_key, bg="green")
genkey_btn.place(x=180, y=30)


window.mainloop()



