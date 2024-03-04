from breezypythongui import *
from taxcalculator import *
class PrompterBoxDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Prompter Box Demo", width=300, height=100)
        self.label = self.addLabel(text="", row = 0, column = 0, sticky="NSEW")
        self.addButton(text ="Username", row = 1, column= 0, command = self.getUserName)

    def getUserName(self):
        name = self.prompterBox(title = "Input Dialog", promptString= "Your username:")
        self.label["text"] = "Hi " + name + "!"
        TaxCalculator().mainloop()
        


PrompterBoxDemo().mainloop()