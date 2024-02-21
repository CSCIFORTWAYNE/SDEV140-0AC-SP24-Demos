from breezypythongui import EasyFrame
#other imports

class CounterDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Counter Demo")
        self.setSize(200,75)
        self.count = 0
        self.label = self.addLabel(text="0", row=0, column=0, sticky="NSEW", columnspan=2)
        self.addButton(text="Next", row=1, column=0, command=self.next)
        self.addButton(text="Reset", row=1, column=1, command=self.reset)
    def next(self):
        self.count += 1
        self.label["text"] = str(self.count)
    def reset(self):
        self.count = 0
        self.label["text"] = str(self.count)
        # add other widgets to the window
    #Add definitions of event handlers

def main():
    CounterDemo().mainloop()

if __name__ == "__main__":
    main()