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

        MainFrame = Frame(self.root, bd=10, width=1920, height=900, relief=RIDGE)
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


        RightFrame1 = Frame(TopFrame2,bd=5, width=320, height=400,padx=0, relief=RIDGE)
        RightFrame1.pack(side=RIGHT) 

        RightFrame1a = Frame(RightFrame1, bd=5, width=310, height=300, padx=0, relief=RIDGE)
        RightFrame1a.pack(side=TOP) 

        RightFrame2 = Frame(TopFrame2, bd=5, width=300, height=400, padx=0,relief=RIDGE)
        RightFrame2.pack(side=RIGHT)  

        RightFrame2a = Frame(RightFrame2,bd=5, width=280, height=50, padx=0, relief=RIDGE)
        RightFrame2a.pack(side=TOP) 

        RightFrame2b = Frame(RightFrame2,bd=5, width=280, height=180, padx=0, relief=RIDGE)
        RightFrame2b.pack(side=TOP) 

        RightFrame2c = Frame(RightFrame2,bd=5, width=280, height=100, padx=0, relief=RIDGE)
        RightFrame2c.pack(side=TOP) 

        RightFrame2d = Frame(RightFrame2,bd=5, width=280, height=50, padx=0, relief=RIDGE)
        RightFrame2d.pack(side=TOP) 

        # -------------------------------Text Buttons--------------------------
        self.txtReciept = Text(RightFrame1a, height=22, width=34, bd=10, font=('arial',16,'bold'))
        self.txtReciept.grid(row=0, column=0)

        # -------------------------------Widget Label/Entry--------------------------
        self.lblReference = Label(LeftFrame1, font=('arial',24,'bold'),text = 'Reference', bd=7, anchor='w')
        self.lblReference.grid(row=0, column=0, sticky=W)
        self.txtRefernce = Entry(LeftFrame1, font=('arial',24,'bold'), bd=5, width=40, justify='left')
        self.txtRefernce.grid(row=0, column=1)

        self.lblFirstName = Label(LeftFrame1, font=('arial',24,'bold'),text = 'First Name', bd=7, anchor='w')
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(LeftFrame1, font=('arial',24,'bold'), bd=5, width=40, justify='left')
        self.txtFirstName.grid(row=1, column=1)

        self.lblSurname = Label(LeftFrame1, font=('arial',24,'bold'),text = 'Surname', bd=7, anchor='w')
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname= Entry(LeftFrame1, font=('arial',24,'bold'), bd=5, width=40, justify='left')
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(LeftFrame1, font=('arial',24,'bold'),text = 'Address', bd=7, anchor='w')
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame1, font=('arial',24,'bold'), bd=5, width=40, justify='left')
        self.txtAddress.grid(row=3, column=1)

        self.lblGender = Label(LeftFrame1, font=('arial',24,'bold'),text = 'Gender', bd=7, anchor='w')
        self.lblGender.grid(row=4, column=0, sticky=W)
        self.txtGender= Entry(LeftFrame1, font=('arial',24,'bold'), bd=5, width=40, justify='left')
        self.txtGender.grid(row=4, column=1)

        self.lblMobile = Label(LeftFrame1, font=('arial',24,'bold'),text = 'Mobile', bd=7, anchor='w')
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile= Entry(LeftFrame1, font=('arial',24,'bold'), bd=5, width=40, justify='left')
        self.txtMobile.grid(row=5, column=1)

        #---------------------------------Widget Label/Entry----------------------- 
        self.lblCityWeighting = Label(LeftFrame2left, font=('arial',24,'bold'),text = 'City Weighting', bd=7, anchor='w')
        self.lblCityWeighting.grid(row=0, column=0, sticky=W)
        self.txtCityWeighting= Entry(LeftFrame2left, font=('arial',24,'bold'), bd=5, width=10, justify='left')
        self.txtCityWeighting.grid(row=0, column=1)      

        self.lblBasicSalary = Label(LeftFrame2left, font=('arial',24,'bold'),text = 'Basic Salary', bd=7, anchor='w')
        self.lblBasicSalary.grid(row=1, column=0, sticky=W)
        self.txtBasicSalary= Entry(LeftFrame2left, font=('arial',24,'bold'), bd=5, width=10, justify='left')
        self.txtBasicSalary.grid(row=1, column=1) 

        self.lblOverTime = Label(LeftFrame2left, font=('arial',24,'bold'),text = 'Over Time', bd=7, anchor='w')
        self.lblOverTime.grid(row=2, column=0, sticky=W)
        self.txtOverTime= Entry(LeftFrame2left, font=('arial',24,'bold'), bd=5, width=10, justify='left')
        self.txtOverTime.grid(row=2, column=1) 

        self.lblOtherPaymentDue= Label(LeftFrame2left, font=('arial',24,'bold'),text = 'Other Payment', bd=7, anchor='w')
        self.lblOtherPaymentDue.grid(row=3, column=0, sticky=W)
        self.txtOtherPaymentDue= Entry(LeftFrame2left, font=('arial',24,'bold'), bd=5, width=10, justify='left')
        self.txtOtherPaymentDue.grid(row=3, column=1) 

        #---------------------------------Widget Label/Entry----------------------- 
        self.lblTax = Label(LeftFrame2right, font=('arial',24,'bold'),text = 'Tax', bd=7, anchor='w')
        self.lblTax.grid(row=0, column=0, sticky=W)
        self.txtTax= Entry(LeftFrame2right, font=('arial',24,'bold'), bd=5, width=12, justify='left')
        self.txtTax.grid(row=0, column=1)      

        self.lblPension = Label(LeftFrame2right, font=('arial',24,'bold'),text = 'Pension', bd=7, anchor='w')
        self.lblPension.grid(row=1, column=0, sticky=W)
        self.txtPension= Entry(LeftFrame2right, font=('arial',24,'bold'), bd=5, width=12, justify='left')
        self.txtPension.grid(row=1, column=1) 

        self.lblstdLoan = Label(LeftFrame2right, font=('arial',24,'bold'),text = 'student Loan', bd=7, anchor='w')
        self.lblstdLoan.grid(row=2, column=0, sticky=W)
        self.txtstdLoan= Entry(LeftFrame2right, font=('arial',24,'bold'), bd=5, width=12, justify='left')
        self.txtstdLoan.grid(row=2, column=1) 

        self.lblNIPayment= Label(LeftFrame2right, font=('arial',24,'bold'),text = 'NI   Payment', bd=7, anchor='w')
        self.lblNIPayment.grid(row=3, column=0, sticky=W)
        self.txtNIPayment= Entry(LeftFrame2right, font=('arial',24,'bold'), bd=5, width=12, justify='left')
        self.txtNIPayment.grid(row=3, column=1) 

        #---------------------------------Widget Label/Entry----------------------- 
        self.lblPayday = Label(RightFrame2a, font=('arial',24,'bold'),text = 'Payday', bd=5, anchor='w')
        self.lblPayday.grid(row=0, column=0, sticky=W)
        self.txtPayday= Entry(RightFrame2a, font=('arial',24,'bold'), bd=5, width=20, justify='left')
        self.txtPayday.grid(row=0, column=1) 

        self.lblTaxPeriod = Label(RightFrame2b, font=('arial',24,'bold'),text = 'Tax Period', bd=5, anchor='w')
        self.lblTaxPeriod.grid(row=0, column=0, sticky=W)
        self.txtTaxPeriod= Entry(RightFrame2b, font=('arial',24,'bold'), bd=5, width=17, justify='left')
        self.txtTaxPeriod.grid(row=0, column=1)

        self.lblTaxCode = Label(RightFrame2b, font=('arial',24,'bold'),text = 'TaxCode', bd=5, anchor='w')
        self.lblTaxCode.grid(row=1, column=0, sticky=W)
        self.txtTaxCode= Entry(RightFrame2b, font=('arial',24,'bold'), bd=5, width=17, justify='left')
        self.txtTaxCode.grid(row=1, column=1)

        self.lblNINumber = Label(RightFrame2b, font=('arial',24,'bold'),text = 'NI Number', bd=5, anchor='w')
        self.lblNINumber.grid(row=2, column=0, sticky=W)
        self.txtNINumber= Entry(RightFrame2b, font=('arial',24,'bold'), bd=5, width=17, justify='left')
        self.txtNINumber.grid(row=2, column=1)

        self.lblNICode = Label(RightFrame2b, font=('arial',24,'bold'),text = 'NI Code', bd=5, anchor='w')
        self.lblNICode.grid(row=3, column=0, sticky=W)
        self.txtNICode= Entry(RightFrame2b, font=('arial',24,'bold'), bd=5, width=17, justify='left')
        self.txtNICode.grid(row=3, column=1)

        self.lblTaxablePay = Label(RightFrame2c, font=('arial',24,'bold'),text = 'Taxable Pay', bd=5, anchor='w')
        self.lblTaxablePay.grid(row=0, column=0, sticky=W)
        self.txtTaxablePay= Entry(RightFrame2c, font=('arial',24,'bold'), bd=5, width=12, justify='left')
        self.txtTaxablePay.grid(row=0, column=1)

        self.lblPensionablePay = Label(RightFrame2c, font=('arial',24,'bold'),text = 'Pensionable Pay', bd=5, anchor='w')
        self.lblPensionablePay.grid(row=1, column=0, sticky=W)
        self.txtPensionablePay= Entry(RightFrame2c, font=('arial',24,'bold'), bd=5, width=12, justify='left')
        self.txtPensionablePay.grid(row=1, column=1) 

        self.lblNetPay = Label(RightFrame2d, font=('arial',24,'bold'),text = 'Net Pay', bd=5, anchor='w')
        self.lblNetPay.grid(row=0, column=0, sticky=W)
        self.txtNetPay= Entry(RightFrame2d, font=('arial',24,'bold'), bd=5, width=17, justify='left')
        self.txtNetPay.grid(row=0, column=1) 

        self.lblGrossPay = Label(RightFrame2d, font=('arial',24,'bold'),text = 'Gross Pay', bd=5, anchor='w')
        self.lblGrossPay.grid(row=1, column=0, sticky=W)
        self.txtGrossPay= Entry(RightFrame2d, font=('arial',24,'bold'), bd=5, width=17, justify='left')
        self.txtGrossPay.grid(row=1, column=1)    
        
        self.lblDeductions = Label(RightFrame2d, font=('arial',24,'bold'),text = 'Deductions', bd=5, anchor='w')
        self.lblDeductions.grid(row=2, column=0, sticky=W)
        self.txtDeductions= Entry(RightFrame2d, font=('arial',24,'bold'), bd=5, width=17, justify='left')
        self.txtDeductions.grid(row=2, column=1)   

        #---------------------------------Widget TreeView----------------------- 
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('TKDefaultFont',18))
        style.configure('Treeview',rowheight =40, font=('TKDefaultFont',18))

        treeview_columns = ('Reference','Firstname','Surname','Address','Gender','Mobile','NI Number','Student Loan',
                            'Tax','Pension','Deductions','Net Pay','Gross Pay')
        
        treeview = ttk.Treeview(TopFrame3, column= treeview_columns, show='headings',height=7)
        treeview.pack()

        #set up the treeview Columns
        for col in treeview_columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=145)
            treeview.column(col, anchor='center')

        #Load data from excel onto the Treeview

        try:
            df = pd.read_excel('Emp.xlsx')
            for index, row in df.iterrows():
                treeview.insert('','end', values= (row['Reference'], row['Firstname'], row['Surname'], row['Address']
                                                    , row['Gender'], row['Mobile'], row['NI Number']
                                                    , row['Student loan'], row['Tax'], row['Pension']
                                                    , row['Deductions'], row['Net Pay'], row['Gross Pay']
                                                    ))
        except Exception as  e:
            tkinter.messagebox.showerror('Error',str(e))
        #---------------------------------Widget Label/Entry----------------------- 
        # Function to handle the Treeview row selection event
        def on_treeview_select(event):
            selcted_item = treeview.focus()
            if selcted_item:
                values = treeview.item(selcted_item, 'values')
                self.txtRefernce.delete(0,END)
                self.txtFirstName.delete(0,END)
                self.txtSurname.delete(0,END)
                self.txtAddress.delete(0,END)
                self.txtGender.delete(0,END)
                self.txtMobile.delete(0,END)
                self.txtNINumber.delete(0,END)
                self.txtstdLoan.delete(0,END)
                self.txtTax.delete(0,END)
                self.txtPension.delete(0,END)
                self.txtDeductions.delete(0,END)
                self.txtNetPay.delete(0,END)
                self.txtGrossPay.delete(0,END)  

                self.txtRefernce.insert(0, values[0])
                self.txtFirstName.insert(0, values[1])
                self.txtSurname.insert(0, values[2])
                self.txtAddress.insert(0, values[3])
                self.txtGender.insert(0, values[4])
                self.txtMobile.insert(0, values[5])
                self.txtNINumber.insert(0, values[6])
                self.txtstdLoan.insert(0, values[7])
                self.txtTax.insert(0, values[8])
                self.txtPension.insert(0, values[9])
                self.txtDeductions.insert(0, values[10])
                self.txtNetPay.insert(0, values[11])
                self.txtGrossPay.insert(0, values[12])

        treeview.bind('<<TreeviewSelect>>',on_treeview_select)
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