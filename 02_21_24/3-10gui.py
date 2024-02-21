from breezypythongui import EasyFrame
#other imports

class MonthlyPayment(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Monthly Payment Calculator")
        # add other widgets to the window
        self.purchasePrice = 0.0
        self.downPayment = 0.0
        self.monthlyPayment = 0.0
        self.addLabel(text="Purchase Price",row=0, column=0)
        self.addLabel(text="Down Payment",row=1, column=0)
        self.addLabel(text="Annual Interest%", row=2, column=0)
        self.addLabel(text="Monthly Payment", row=3, column=0)
        self.price = self.addFloatField(value=0.0,row=0, column=1,precision=2)
        self.down = self.addFloatField(value = 0.0, row=1, column=1,state="readonly",precision=2)
        self.interest = self.addIntegerField(value=12,row=2, column=1,state="readonly")
        self.monthly = self.addFloatField(value=0.0,row=3,column=1,state="readonly",precision=2)
        self.compute = self.addButton(text="Compute", row = 4, column=0, columnspan=2, command=self.compute)
        self.outputArea = self.addTextArea("",row=5,column=0, columnspan=2,width=85,height=15)
        self.outputArea["state"] = "disabled"

    def compute(self):
        self.purchasePrice = self.price.getNumber()
        if self.purchasePrice == 0:
            return
        self.downPayment = self.purchasePrice * .1
        self.monthlyPayment = (self.purchasePrice - self.downPayment) * .05
        self.down.setNumber(self.downPayment)
        self.monthly.setNumber(self.monthlyPayment)
        self.outputArea["state"] = "normal"
        #Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance
        self.outputArea.setText("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance\n")
        monthlyInterestRate = .12/12
        month = 1
        startBalance = self.purchasePrice - self.downPayment
        interestToPay = startBalance * monthlyInterestRate
        principal = self.monthlyPayment - interestToPay
        endingBalance = startBalance - principal
        while endingBalance >= self.monthlyPayment:
            self.outputArea.appendText(" %-4d  %10.2f        %7.2f          %7.2f          %7.2f    %13.2f\n"%(month,startBalance,interestToPay,principal,self.monthlyPayment,endingBalance))
            month +=1
            startBalance = endingBalance
            interestToPay = startBalance * monthlyInterestRate
            principal = self.monthlyPayment - interestToPay
            endingBalance = startBalance - principal
        
        self.outputArea.appendText(" %-4d  %10.2f        %7.2f          %7.2f          %7.2f    %13.2f\n"%(month,startBalance,interestToPay,principal,self.monthlyPayment,endingBalance))
        month += 1
        startBalance = endingBalance
        interestToPay = startBalance * monthlyInterestRate
        principal = startBalance
        self.monthlyPayment = startBalance + interestToPay
        endingBalance = 0
        self.outputArea.appendText(" %-4d  %10.2f        %7.2f          %7.2f          %7.2f    %13.2f\n"%(month,startBalance,interestToPay,principal,self.monthlyPayment,endingBalance))

    #Add definitions of event handlers

def main():
    MonthlyPayment().mainloop()

if __name__ == "__main__":
    main()