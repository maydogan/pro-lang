from Tkinter import *

class May:
    def __init__(self):
        self.etiket = Label(text = "Dosyayı silmek istediğinize emin misiniz?")
        self.etiket.pack()

win = Tk()
app = May()
mainloop()
