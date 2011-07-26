from Tkinter import * 

class May:
    def __init__(self, master):
        mount = Frame(master)
        mount.pack()

        self.button = Button(mount, text="QUIT", fg="red",command = mount.quit)
        self.button.pack(side=RIGHT)
        
        self.hello = Button(mount, text="HELLO", fg="yellow", command = self.hi_say)
        self.hello.pack(side=RIGHT)

    def hi_say(self):
        print "Hi! What's up ?"

root = Tk()

may = May(root)

root.mainloop()


