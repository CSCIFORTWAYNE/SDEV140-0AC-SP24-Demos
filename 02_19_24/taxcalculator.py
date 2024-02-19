from breezypythongui import EasyFrame
#other imports

class TaxCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.setTitle("Tax Calculator")
        # add other widgets to the window
        self.addLabel(text="Gross Income", row=0, column=0)
        self.addLabel(text="Dependents",row=1, column=0)
        self.addLabel(text="Total Tax",row=3,column=0)
        self.income = self.addFloatField(value = 0.0,row=0,column=1,precision=2)
        self.dependents = self.addIntegerField(value=0,row=1,column=1, width=20)
        self.computeBtn = self.addButton(text="Compute", row=2,column=1, command=self.compute)
        
        self.totalTax = self.addFloatField(value=0.0,precision=2,row=3, column=1,state="readonly")
    def compute(self):
        TAX_RATE = 0.20
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0

        grossIncome = self.income.getNumber()
        numDependents = self.dependents.getNumber()
        taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
        incomeTax = taxableIncome * TAX_RATE
        self.totalTax.setNumber(incomeTax)

    #Add definitions of event handlers

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()