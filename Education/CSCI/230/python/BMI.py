""" gradeCalc.py
    calculate grades with a GUI
"""

from Tkinter import *

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
class App(Tk):
  def __init__(self):
    Tk.__init__(self)

    self.headerFont = ("Helvetica", "16", "bold")
    self.title("Body Mass Index Calculator")
    self.addInputs()
    self.addOutput()
    
  def addInputs(self):    
    Label(self, text = "", width = 35).grid(columnspan = 2)
    Label(self, text = "Height",font = self.headerFont).grid(row = 1, columnspan = 2)
    
    Label(self, text = "Feet").grid(row = 2, column = 0)
    self.feet = Entry(self)
    self.feet.grid(row = 2, column = 1)
    self.feet.insert(0, "")
    
    Label(self, text = "Inches").grid(row = 3, column = 0)
    self.inches = Entry(self)
    self.inches.grid(row = 3, column = 1)
    self.inches.insert(0, "")
    
    Label(self, text = "").grid(row = 4, columnspan = 2)
    Label(self, text = "Weight", font = self.headerFont).grid(row = 5, columnspan = 2)

    Label(self, text = "Pounds").grid(row = 6, column = 0)
    self.lbs = Entry(self)
    self.lbs.grid(row = 6, column = 1)
    self.lbs.insert(0, "")
    
    Label(self, text = "").grid(row = 7, columnspan = 2)

    
  def addOutput(self):
    self.btnCalc = Button(self, text = "Calculate BMI", font = self.headerFont)
    self.btnCalc.grid(row = 8, columnspan = 2)
    self.btnCalc["command"] = self.calculate
    
    Label(self, text = "").grid(row = 9, columnspan = 2)
    self.desc = Label(self, text = " Click the \"Calculate BMI\" Button \n to display your BMI and Status ")
    self.desc.grid(row = 10, columnspan = 2)
    Label(self, text = "").grid(row = 11, columnspan = 2)
    
    
  def calculate(self):
    
    #lab1 = int(self.txtLab1.get())
    #self.lblLabs["text"] = "%.2f" % labPerc    
    global isInt;
    
    if not( isInt(self.feet.get()) ) or not (isInt(self.inches.get()) ) or not (isInt(self.lbs.get()) ):
        #print self.feet.get() + " " + self.inches.get() + " " + self.lbs.get()
        toplevel = Toplevel()
        label1 = Label(toplevel, text=" Please Enter Valid Integers for Height and Weight", height=10, width=55)
        label1.pack()
        return;
    
    height = float(self.feet.get()) * 12 + float(self.inches.get());
    weight = float(self.lbs.get())
    
    bmiScore = weight * 703 /  height**2
    
    bmiScore = float("{0:.2f}".format(round(bmiScore,2)))
    
    if(bmiScore <= 18.50):
        status = "Underweight";
    elif(bmiScore > 18.50) and (bmiScore <= 24.9):
        status = "Normal";
    elif(bmiScore > 24.9) and (bmiScore <= 29.9):
        status = "Overweight";
    elif(bmiScore > 29.0):
        status = "Obese";
    else:
        status = "Dunno";
    
    
    self.desc["text"] = "YES ";
    self.btnCalc["text"] = "Re-Calculate BMI";
    
    
    Label(self, text = "Your BMI").grid(row = 10, column = 0)
    self.BMI = Entry(self)
    self.BMI.grid(row = 10, column = 1)
    self.BMI.insert(0, str(bmiScore))
    
    Label(self, text = "Your Status").grid(row = 11, column = 0)
    self.STAT = Entry(self)
    self.STAT.grid(row = 11, column = 1)
    self.STAT.insert(0, status)
    
    
    
    Label(self, text = "").grid(row = 12, columnspan = 2)
    
def main():
  app = App()
  app.mainloop()

if __name__ == "__main__":
  main()