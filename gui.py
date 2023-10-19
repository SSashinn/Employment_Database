from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os 
import pandas as pd

class Employee:

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Database Management System")
        self.root.geometry("1920x1000+0+0")
        self.root.configure(bg = 'gainsboro')

        MainFrame = Frame(self.root, bd=10, width=1920, height=9000, relief=RIDGE)
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame, bd=7, width=1910, height=50, relief=RIDGE)
        TopFrame1.grid(row=0, column=0)
        
        TopFrame2 = Frame(MainFrame,bd=7, width=1910, height=100, relief=RIDGE)
        TopFrame2.grid(row=1, column=0)

        TopFrame3 = Frame(MainFrame,bd=7, width=1910, height=500, relief=RIDGE)
        TopFrame3.grid(row=2, column=0)        
        
        LeftFrame = Frame(TopFrame2,bd=5, width=1910, height=400, relief=RIDGE)
        LeftFrame.pack(side=LEFT) 

        LeftFrame1 = Frame(LeftFrame, bd=5, width=900, height=180, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP) 

        LeftFrame2 = Frame(LeftFrame,bd=5, width=900, height=180, relief=RIDGE)
        LeftFrame2.pack(side=TOP)  

        LeftFrame2left = Frame(LeftFrame2,bd=5, width=300, height=170, relief=RIDGE)
        LeftFrame2left.pack(side=LEFT) 

        LeftFrame2right = Frame(LeftFrame2,bd=5, width=300, height=170, relief=RIDGE)
        LeftFrame2right.pack(side=RIGHT)  


        RightFrame1 = Frame(TopFrame2,bd=5, width=320, height=400,padx=0, bg='gainsboro', relief=RIDGE)
        RightFrame1.pack(side=RIGHT) 

        RightFrame1a = Frame(RightFrame1, bd=5, width=310, height=300, padx=0, bg='gainsboro', relief=RIDGE)
        RightFrame1a.pack(side=TOP) 

        RightFrame2 = Frame(TopFrame2, bd=5, width=300, height=400, padx=0, bg='gainsboro', relief=RIDGE)
        RightFrame2.pack(side=RIGHT)  

        RightFrame2a = Frame(RightFrame2,bd=5, width=280, height=50, padx=0, bg='gainsboro', relief=RIDGE)
        RightFrame2a.pack(side=TOP) 

        RightFrame2b = Frame(RightFrame2,bd=5, width=280, height=180, padx=0, bg='gainsboro', relief=RIDGE)
        RightFrame2b.pack(side=TOP) 

        RightFrame2c = Frame(RightFrame2,bd=5, width=280, height=100, padx=0, bg='gainsboro', relief=RIDGE)
        RightFrame2c.pack(side=TOP) 

        RightFrame2d = Frame(RightFrame2,bd=5, width=280, height=50, padx=0, bg='gainsboro', relief=RIDGE)
        RightFrame2d.pack(side=TOP) 
        #---------------------------------Widget Buttons----------------------- 
        self.btnAddNewTotal = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',20,'bold'), padx=1,
                                width = 15,text ="AddNew/Total").grid(row=0,column=0)
        
        self.btnPrint = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',20,'bold'), padx=1,
                            width = 15,text ="Print").grid(row=0,column=1)        
        
        self.btnDisplay = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',20,'bold'), padx=1,
                                width = 15,text ="Display").grid(row=0,column=2)

        self.btnUpdate = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',20,'bold'), padx=1,
                                 width = 15,text ="Update").grid(row=0,column=3)

        self.btnDelete = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',20,'bold'), padx=1,
                                width = 15,text ="Delete").grid(row=0,column=4)
        
        self.btnReset = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',20,'bold'), padx=1,
                            width = 15,text ="Reset").grid(row=0,column=5)        
        
        self.btnExit = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',20,'bold'), padx=1,
                                width = 15,text ="Exit").grid(row=0,column=6)


if __name__ == '__main__':
    # creating tkinter window 
    root = Tk()
    # Giving the window properties
    application = Employee(root)
    # Execute Tkinter 
    root.mainloop()