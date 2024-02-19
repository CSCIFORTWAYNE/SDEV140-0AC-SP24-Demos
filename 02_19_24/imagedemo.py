from breezypythongui import EasyFrame
#other imports
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False)
        # add other widgets to the window
        imageLabel = self.addLabel(text = "", row = 0, column= 0, sticky="NSEW")
        textLabel = self.addLabel(text="Hello IT, Have you tried turning it off and on again?", row= 1, column=0, sticky="NSEW")
        
        self.image = PhotoImage(file = "it.gif")
        imageLabel["image"] = self.image
        myfont = Font(family = "Veranda", size = 20, slant = "italic")
        textLabel["font"] = myfont
        textLabel["foreground"] = "blue"

    #Add definitions of event handlers

def main():
    ImageDemo().mainloop()

if __name__ == "__main__":
    main()