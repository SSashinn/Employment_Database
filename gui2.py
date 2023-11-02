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
        self.root.geometry("1100x600+0+0")
        self.root.configure(bg = 'gainsboro') #To Change properties after initiazlization.
        self.root.attributes('-fullscreen', True)

        MainFrame = Frame(self.root, bd=11, width=1100, height=600, relief=RIDGE)
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame, bd=7, width=1329, height=50, relief=RIDGE)
        TopFrame1.grid(row=0, column=0)
        
        TopFrame2 = Frame(MainFrame,bd=7, width=1329, height=110, relief=RIDGE)
        TopFrame2.grid(row=1, column=0)

        TopFrame3 = Frame(MainFrame,bd=7, width=1329, height=300, relief=RIDGE)
        TopFrame3.grid(row=2, column=0)        
        
        LeftFrame = Frame(TopFrame2,bd=5, width=1329, height=200, relief=RIDGE)
        LeftFrame.pack(side=LEFT) 

        LeftFrame1 = Frame(LeftFrame, bd=5, width=626, height=100, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP) 

        LeftFrame2 = Frame(LeftFrame,bd=5, width=626, height=300, relief=RIDGE)
        LeftFrame2.pack(side=TOP)  

        LeftFrame2left = Frame(LeftFrame2,bd=5, width=300, height=170, relief=RIDGE)
        LeftFrame2left.pack(side=LEFT) 

        LeftFrame2right = Frame(LeftFrame2,bd=5, width=300, height=170, relief=RIDGE)
        LeftFrame2right.pack(side=RIGHT)  


        RightFrame1 = Frame(TopFrame2,bd=5, width=320, height=150,padx=0, relief=RIDGE)
        RightFrame1.pack(side=RIGHT) 

        RightFrame1a = Frame(RightFrame1, bd=5, width=311, height=100, padx=0, relief=RIDGE)
        RightFrame1a.pack(side=TOP) 

        RightFrame2 = Frame(TopFrame2, bd=5, width=300, height=200, padx=0,relief=RIDGE)
        RightFrame2.pack(side=RIGHT)  

        RightFrame2a = Frame(RightFrame2,bd=5, width=400, height=50, padx=0, relief=RIDGE)
        RightFrame2a.pack(side=TOP) 

        RightFrame2b = Frame(RightFrame2,bd=5, width=400, height=300, padx=0, relief=RIDGE)
        RightFrame2b.pack(side=TOP) 

        RightFrame2c = Frame(RightFrame2,bd=5, width=400, height=110, padx=0, relief=RIDGE)
        RightFrame2c.pack(side=TOP) 

        RightFrame2d = Frame(RightFrame2,bd=5, width=400, height=50, padx=0, relief=RIDGE)
        RightFrame2d.pack(side=TOP) 

        # -------------------------------Variables--------------------------
        global Ed
        Refernce  = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()
        cityWeighting = IntVar()
        basicSalary = IntVar()
        OverTime = StringVar()
        GrossPay = StringVar()
        NetPay = StringVar()
        Tax = StringVar()
        Pension = StringVar()
        stdLoan = StringVar()
        NIpayment = StringVar()
        Deductions = StringVar()    
        Payday = StringVar()
        TaxPeriod = StringVar()
        NINumber = StringVar()
        NICode = StringVar()
        TaxablePay = StringVar()
        PensionablePay = StringVar()
        OtherPaymentDue  = StringVar()
        TaxCode = StringVar()
       
        cityWeighting.set("0.00")
        basicSalary.set("0.00")
        OtherPaymentDue.set("0.00")
        OverTime.set("0.00")

        # -------------------------------Functions--------------------------
        # This function will delete data from excel
        def deleteData(Reference):
            # delete data from excel
            delPopup = tkinter.messagebox.askyesno("Delete","Confirm if you want to delete the data")
            if delPopup>0:
                try:
                    df = pd.read_excel("Emp.xlsx")
                    df.drop(df[df['Reference'] == Reference].index, inplace=True)
                    df.to_excel("Emp.xlsx", index=False)
                    tkinter.messagebox.showinfo("Success", "Record deleted successfully.")
                except Exception as  e:
                    tkinter.messagebox.showerror('Error',str(e))

                # Delete data From Treeview
                selected_item = treeview.selection()
                if selected_item:
                    item_text = treeview.item(selected_item, "values")[0]
                    df.drop(df[df['Reference'] == item_text].index, inplace=True)
                    treeview.delete(selected_item)    


        def reset():
            cityWeighting.set("0.00")
            basicSalary.set("0.00")
            OtherPaymentDue.set("0.00")
            OverTime.set("0.00")        

            Refernce.set("")
            FirstName.set("")
            Surname.set("")
            Address.set("")
            Gender.set("")
            Mobile.set("")
            GrossPay.set("")
            NetPay.set("")
            Tax.set("")
            Pension.set("")
            stdLoan.set("")
            NIpayment.set("")
            Deductions.set("")
            Payday.set("")
            TaxPeriod.set("")
            NINumber.set("")
            NICode.set("")
            TaxablePay.set("")
            PensionablePay.set("")
            TaxCode.set("")
            self.txtReciept.delete("1.0",END)


        def quit():
            quit = tkinter.messagebox.askyesno("Employee Database Management System", "Confirm if you want to quit")
            if quit>0:
                root.destroy()
                return
            

        def payReference():
            Payday.set(time.strftime("%d/%m/%y"))
            refPay = random.randint(14572, 700532)
            Refernce.set(str(refPay))

            NIpay = random.randint(31101, 400573)
            NINumber.set(NIpay)

            idate = datetime.datetime.now()
            TaxPeriod.set(idate.month)

            nCode = random.randint(1111, 11573)
            NICode.set("NIC"+str(nCode))

            itaxCode = random.randint(7472, 14773)
            TaxCode.set("TCode"+str(itaxCode))
            monthlySalary()


        def monthlySalary():
            CW = float(cityWeighting.get())
            BS = float(basicSalary.get())
            OT = float(OverTime.get())
            PD = float(OtherPaymentDue.get())

            MTax = str('₹%.2f'%((BS + CW + OT + PD)* 0.3))
            Tax.set(MTax)

            MPension = str('₹%.2f'%((BS + CW + OT + PD)* 0.2))
            Pension.set(MPension)

            MStdLoan = str('₹%.2f'%((BS + CW + OT + PD)* 0.022))
            stdLoan.set(MStdLoan)

            MNIPayment = str('₹%.2f'%((BS + CW + OT + PD)* 0.011))
            NIpayment.set(MNIPayment)

            sum = BS + CW + OT + PD
            MDeduct = (sum*0.3)+(sum*0.2)+(sum*0.022)+(sum*0.011)
            Deductions.set(str('₹%.2f'%(MDeduct)))

            GrossPay.set(str('₹%.2f'%(sum)))
            NetPay.set(str('₹%.2f'%(sum-MDeduct)))
            TaxablePay.set(MTax)
            PensionablePay.set(MPension)
            # display()


        def display():
            self.txtReciept.delete("1.0",END)
            self.txtReciept.insert(END, '\t Monthly Play Slip\n\n','center')
            self.txtReciept.insert(END, 'Reference\t\t\t'+ Refernce.get()+'\n')
            self.txtReciept.insert(END, 'Payday\t\t\t'+ Payday.get()+'\n')
            self.txtReciept.insert(END, 'Firstname\t\t\t'+ FirstName.get()+'\n')
            self.txtReciept.insert(END, 'surname\t\t\t'+ Surname.get()+'\n')
            self.txtReciept.insert(END, 'Tax\t\t\t'+ Tax.get()+'\n')
            self.txtReciept.insert(END, 'Pension\t\t\t'+ Pension.get()+'\n')
            self.txtReciept.insert(END, 'Student Loan\t\t\t'+ stdLoan.get()+'\n')
            self.txtReciept.insert(END, 'NI Number\t\t\t'+ NINumber.get()+'\n')
            self.txtReciept.insert(END, 'NI Payment\t\t\t'+ NIpayment.get()+'\n')
            self.txtReciept.insert(END, 'Deductuions\t\t\t'+ Deductions.get()+'\n')
            self.txtReciept.insert(END, 'City Weighting\t\t\t'+ str('₹ %.2f'%(cityWeighting.get()))+'\n')

            self.txtReciept.insert(END, '\nTax Paid\t\t\t'+ str('₹ %.2f'%(basicSalary.get()))+'\n')
            self.txtReciept.insert(END, 'OverTime\t\t\t₹'+ OverTime.get()+'\n')
            self.txtReciept.insert(END, 'NetPay\t\t\t'+ NetPay.get()+'\n')
            self.txtReciept.insert(END, 'GrossPay\t\t\t'+ GrossPay.get()+'\n')


        def iprint():
            q = self.txtReciept.get("1.0","end-1c")
            filename = tempfile.mktemp(".doc")
            open(filename, "w").write(q)
            os.startfile(filename,"print")


        def addData():
            try:
                df = pd.read_excel('Emp.xlsx')
                Reference = self.txtRefernce.get()
                new_data = {
                    'Reference':[Reference], 
                    'Firstname': [self.txtFirstName.get()],
                    'Surname':[self.txtSurname.get()],
                    'Address':[self.txtAddress.get()],
                    'Gender':[self.txtGender.get()], 
                    'Mobile':[self.txtMobile.get()],
                    'NI Number':[self.txtNINumber.get()],
                    'Student loan':[self.txtstdLoan.get()],
                    'Tax':[self.txtTax.get()],
                    'Pension':[self.txtPension.get()],
                    'Deductions':[self.txtDeductions.get()],
                    'Net Pay':[self.txtNetPay.get()],
                    'Gross Pay':[self.txtGrossPay.get()]
                }
                new_df = pd.DataFrame(new_data)
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_excel("Emp.xlsx", index = False)
                tkinter.messagebox.showinfo('Succesfull','Data updated successfully.')    
                # Delete all item from treeview
                for item in treeview.get_children():
                    treeview.delete(item)

                # Reprint the data from Treeview
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
            except Exception as  e:
                tkinter.messagebox.showerror('Error',str(e))           

        # -------------------------------Text Buttons--------------------------
        self.txtReciept = Text(RightFrame1a, height=22, width=34, bd=11, font=('arial',10,'bold'))
        self.txtReciept.grid(row=0, column=0)

        # -------------------------------Widget Label/Entry--------------------------
        self.lblReference = Label(LeftFrame1, font=('arial',11,'bold'),text = 'Reference', bd=7, anchor='w')
        self.lblReference.grid(row=0, column=0, sticky=W)
        self.txtRefernce = Entry(LeftFrame1, font=('arial',11,'bold'), bd=5, width=40, justify='left',
                                 textvariable= Refernce)
        self.txtRefernce.grid(row=0, column=1)

        self.lblFirstName = Label(LeftFrame1, font=('arial',11,'bold'),text = 'First Name', bd=7, anchor='w')
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(LeftFrame1, font=('arial',11,'bold'), bd=5, width=40, justify='left',
                                  textvariable= FirstName)
        self.txtFirstName.grid(row=1, column=1)

        self.lblSurname = Label(LeftFrame1, font=('arial',11,'bold'),text = 'Surname', bd=7, anchor='w')
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname= Entry(LeftFrame1, font=('arial',11,'bold'), bd=5, width=40, justify='left',
                               textvariable= Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(LeftFrame1, font=('arial',11,'bold'),text = 'Address', bd=7, anchor='w')
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame1, font=('arial',11,'bold'), bd=5, width=40, justify='left',
                                textvariable= Address)
        self.txtAddress.grid(row=3, column=1)

        self.lblGender = Label(LeftFrame1, font=('arial',11,'bold'),text = 'Gender', bd=7, anchor='w')
        self.lblGender.grid(row=4, column=0, sticky=W)
        self.txtGender= Entry(LeftFrame1, font=('arial',11,'bold'), bd=5, width=40, justify='left',
                              textvariable= Gender)
        self.txtGender.grid(row=4, column=1)

        self.lblMobile = Label(LeftFrame1, font=('arial',11,'bold'),text = 'Mobile', bd=7, anchor='w')
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile= Entry(LeftFrame1, font=('arial',11,'bold'), bd=5, width=40, justify='left',
                              textvariable= Mobile)
        self.txtMobile.grid(row=5, column=1)

        #---------------------------------Widget Label/Entry----------------------- 
        self.lblCityWeighting = Label(LeftFrame2left, font=('arial',11,'bold'),text = 'City Weighting', bd=7, anchor='w')
        self.lblCityWeighting.grid(row=0, column=0, sticky=W)
        self.txtCityWeighting= Entry(LeftFrame2left, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                                     textvariable = cityWeighting)
        self.txtCityWeighting.grid(row=0, column=1)      

        self.lblBasicSalary = Label(LeftFrame2left, font=('arial',11,'bold'),text = 'Basic Salary', bd=7, anchor='w')
        self.lblBasicSalary.grid(row=1, column=0, sticky=W)
        self.txtBasicSalary= Entry(LeftFrame2left, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                                   textvariable= basicSalary)
        self.txtBasicSalary.grid(row=1, column=1) 

        self.lblOverTime = Label(LeftFrame2left, font=('arial',11,'bold'),text = 'Over Time', bd=7, anchor='w')
        self.lblOverTime.grid(row=2, column=0, sticky=W)
        self.txtOverTime= Entry(LeftFrame2left, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                                textvariable= OverTime)
        self.txtOverTime.grid(row=2, column=1) 

        self.lblOtherPaymentDue= Label(LeftFrame2left, font=('arial',11,'bold'),text = 'Other Payment', bd=7, anchor='w')
        self.lblOtherPaymentDue.grid(row=3, column=0, sticky=W)
        self.txtOtherPaymentDue= Entry(LeftFrame2left, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                                       textvariable= OtherPaymentDue)
        self.txtOtherPaymentDue.grid(row=3, column=1) 

        #---------------------------------Widget Label/Entry----------------------- 
        self.lblTax = Label(LeftFrame2right, font=('arial',11,'bold'),text = 'Tax', bd=7, anchor='w')
        self.lblTax.grid(row=0, column=0, sticky=W)
        self.txtTax= Entry(LeftFrame2right, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                           textvariable= Tax)
        self.txtTax.grid(row=0, column=1)      

        self.lblPension = Label(LeftFrame2right, font=('arial',11,'bold'),text = 'Pension', bd=7, anchor='w')
        self.lblPension.grid(row=1, column=0, sticky=W)
        self.txtPension= Entry(LeftFrame2right, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                               textvariable= Pension)
        self.txtPension.grid(row=1, column=1) 

        self.lblstdLoan = Label(LeftFrame2right, font=('arial',11,'bold'),text = 'Student Loan', bd=7, anchor='w')
        self.lblstdLoan.grid(row=2, column=0, sticky=W)
        self.txtstdLoan= Entry(LeftFrame2right, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                               textvariable= stdLoan)
        self.txtstdLoan.grid(row=2, column=1) 

        self.lblNIPayment= Label(LeftFrame2right, font=('arial',11,'bold'),text = 'NI Payment', bd=7, anchor='w')
        self.lblNIPayment.grid(row=3, column=0, sticky=W)
        self.txtNIPayment= Entry(LeftFrame2right, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                                 textvariable= NIpayment)
        self.txtNIPayment.grid(row=3, column=1) 

        #---------------------------------Widget Label/Entry----------------------- 
        self.lblPayday = Label(RightFrame2a, font=('arial',11,'bold'),text = 'Payday', bd=5, anchor='w')
        self.lblPayday.grid(row=0, column=0, sticky=W)
        self.txtPayday= Entry(RightFrame2a, font=('arial',11,'bold'), bd=5, width=20, justify='left',
                              textvariable= Payday)
        self.txtPayday.grid(row=0, column=1) 

        self.lblTaxPeriod = Label(RightFrame2b, font=('arial',11,'bold'),text = 'Tax Period', bd=5, anchor='w')
        self.lblTaxPeriod.grid(row=0, column=0, sticky=W)
        self.txtTaxPeriod= Entry(RightFrame2b, font=('arial',11,'bold'), bd=5, width=17, justify='left',
                                 textvariable= TaxPeriod)
        self.txtTaxPeriod.grid(row=0, column=1)

        self.lblTaxCode = Label(RightFrame2b, font=('arial',11,'bold'),text = 'TaxCode', bd=5, anchor='w')
        self.lblTaxCode.grid(row=1, column=0, sticky=W)
        self.txtTaxCode= Entry(RightFrame2b, font=('arial',11,'bold'), bd=5, width=17, justify='left',
                               textvariable= TaxCode)
        self.txtTaxCode.grid(row=1, column=1)

        self.lblNINumber = Label(RightFrame2b, font=('arial',11,'bold'),text = 'NI Number', bd=5, anchor='w')
        self.lblNINumber.grid(row=2, column=0, sticky=W)
        self.txtNINumber= Entry(RightFrame2b, font=('arial',11,'bold'), bd=5, width=17, justify='left',
                                textvariable= NINumber)
        self.txtNINumber.grid(row=2, column=1)

        self.lblNICode = Label(RightFrame2b, font=('arial',11,'bold'),text = 'NI Code', bd=5, anchor='w')
        self.lblNICode.grid(row=3, column=0, sticky=W)
        self.txtNICode= Entry(RightFrame2b, font=('arial',11,'bold'), bd=5, width=17, justify='left',
                              textvariable= NICode)
        self.txtNICode.grid(row=3, column=1)

        self.lblTaxablePay = Label(RightFrame2c, font=('arial',11,'bold'),text = 'Taxable Pay', bd=5, anchor='w')
        self.lblTaxablePay.grid(row=0, column=0, sticky=W)
        self.txtTaxablePay= Entry(RightFrame2c, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                                  textvariable= TaxablePay)
        self.txtTaxablePay.grid(row=0, column=1)

        self.lblPensionablePay = Label(RightFrame2c, font=('arial',11,'bold'),text = 'Pensionable Pay', bd=5, anchor='w')
        self.lblPensionablePay.grid(row=1, column=0, sticky=W)
        self.txtPensionablePay= Entry(RightFrame2c, font=('arial',11,'bold'), bd=5, width=11, justify='left',
                                      textvariable= PensionablePay)
        self.txtPensionablePay.grid(row=1, column=1) 

        self.lblNetPay = Label(RightFrame2d, font=('arial',11,'bold'),text = 'Net Pay', bd=5, anchor='w')
        self.lblNetPay.grid(row=0, column=0, sticky=W)
        self.txtNetPay= Entry(RightFrame2d, font=('arial',11,'bold'), bd=5, width=17, justify='left',
                              textvariable= NetPay)
        self.txtNetPay.grid(row=0, column=1) 

        self.lblGrossPay = Label(RightFrame2d, font=('arial',11,'bold'),text = 'Gross Pay', bd=5, anchor='w')
        self.lblGrossPay.grid(row=1, column=0, sticky=W)
        self.txtGrossPay= Entry(RightFrame2d, font=('arial',11,'bold'), bd=5, width=17, justify='left',
                                textvariable= GrossPay)
        self.txtGrossPay.grid(row=1, column=1)    
        
        self.lblDeductions = Label(RightFrame2d, font=('arial',11,'bold'),text = 'Deductions', bd=5, anchor='w')
        self.lblDeductions.grid(row=2, column=0, sticky=W)
        self.txtDeductions= Entry(RightFrame2d, font=('arial',11,'bold'), bd=5, width=17, justify='left',
                                  textvariable= Deductions)
        self.txtDeductions.grid(row=2, column=1)   

        #---------------------------------Widget TreeView----------------------- 
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('TKDefaultFont',11))
        style.configure('Treeview',rowheight =40, font=('TKDefaultFont',11))

        treeview_columns = ('Reference','Firstname','Surname','Address','Gender','Mobile','NI Number','Student Loan',
                            'Tax','Pension','Deductions','Net Pay','Gross Pay')
        
        treeview = ttk.Treeview(TopFrame3, column= treeview_columns, show='headings',height=7) #Height = no. of rows visible
        treeview.pack()

        #print the treeview Columns Headings
        for col in treeview_columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=70)
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
                self.txtTax.insert(0, values[11])
                self.txtPension.insert(0, values[9])
                self.txtDeductions.insert(0, values[11])
                self.txtNetPay.insert(0, values[11])
                self.txtGrossPay.insert(0, values[11])

        treeview.bind('<<TreeviewSelect>>',on_treeview_select)
        #---------------------------------Widget Buttons----------------------- 
        self.btnAddNewTotal = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',11,'bold'), padx=1,
                                width = 15,text ="Add Total", command=payReference).grid(row=0,column=0)
        
        self.btnPrint = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',11,'bold'), padx=1,
                            width = 15,text ="Print", command=iprint).grid(row=0,column=1)        
        
        self.btnDisplay = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',11,'bold'), padx=1,
                                width = 15,text ="Display", command=display).grid(row=0,column=2)

        self.btnUpdate = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',11,'bold'), padx=1,
                                 width = 15,text ="Update", command=addData).grid(row=0,column=3)

        self.btnDelete = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',11,'bold'), padx=1,
                                width = 15,text ="Delete", command=lambda: deleteData(treeview.item(treeview.selection())
                                ["values"][0])).grid(row=0,column=4)
        
        self.btnReset = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',11,'bold'), padx=1,
                            width = 15,text ="Reset", command=reset).grid(row=0,column=5)        
        
        self.btnExit = Button(TopFrame1,pady=1,bd=4,fg="black", font=('arial',11,'bold'), padx=1,
                                width = 15,text ="Exit", command=quit).grid(row=0,column=6)


if __name__ == '__main__':
    # creating tkinter window 
    root = Tk()
    # Giving the window properties
    application = Employee(root)
    # Execute Tkinter 
    root.mainloop()