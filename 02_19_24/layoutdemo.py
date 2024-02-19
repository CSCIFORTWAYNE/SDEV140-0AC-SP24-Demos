from breezypythongui import EasyFrame
#other imports

class LayoutDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        # add other widgets to the window
        self.addLabel(text="(0, 0)", row = 0, column = 0, sticky="NSEW")
        self.addLabel(text="(0, 1)", row = 0, column = 1, sticky ="NSEW")
        self.addLabel(text="rowspan", row=0, column=2,sticky="NSEW",rowspan=2)
        self.addLabel(text="(1, 0 and 1)", row = 1, column = 0, sticky="NSEW", columnspan=2)
       # self.addLabel(text="(1, 1)", row = 1, column = 1, sticky="SE")
    #Add definitions of event handlers

def main():
    LayoutDemo().mainloop()

if __name__ == "__main__":
    main()