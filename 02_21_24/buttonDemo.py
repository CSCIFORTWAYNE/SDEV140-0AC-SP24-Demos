from breezypythongui import EasyFrame
#other imports

class ButtonDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Button Demo")
        # add other widgets to the window
        self.label = self.addLabel(text="Hello World!", row = 0, column= 0, columnspan=2, sticky="NSEW")
        
        self.clearBtn = self.addButton(text="Clear", row = 1, column=0, command=self.clear)
        self.restoreBtn = self.addButton(text="Restore", row=1, column=1, state="disabled", command=self.restore)
    #Add definitions of event handlers
    def clear(self):
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"
    def restore(self):
        self.label["text"] = "Hello World!"
        self.clearBtn["state"] = "normal"
        self.restoreBtn["state"] = "disabled"

def main():
    ButtonDemo().mainloop()

if __name__ == "__main__":
    main()