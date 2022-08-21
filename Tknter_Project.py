from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hosptal Management System")
        self.root.geometry("1540x800+0+0")

        self.pid = StringVar()
        self.pname = StringVar()
        self.page = StringVar()
        self.pgender = StringVar()
        self.paddres = StringVar()
        self.pdob = StringVar()
        self.adate = StringVar()
        self.pbgpr = StringVar()
        self.did = StringVar()
        self.dname = StringVar()
        self.warno = StringVar()
        self.rmno = StringVar()

        #  ********************************************TITLE********************************************************
        lbltitl = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                        fg="red", bg="white", font=("Time New Roma", 50, "bold"))
        lbltitl.pack(side=TOP, fill=X)

        #  ********************************************FRAMES*******************************************************
        dataframe = Frame(self.root, bd=20, relief=RIDGE)
        dataframe.place(x=0, y=130, width=1350, height=400)

        dataframe_left = LabelFrame(dataframe, bd=10, padx=20, relief=RIDGE,
                                    font=("aral", 12, "bold"), text="Patient Information")
        dataframe_left.place(x=0, y=5, width=900, height=370)

        dataframe_right = LabelFrame(dataframe, bd=10, padx=20, relief=RIDGE,
                                     font=("aral", 12, "bold"), text="Prescription")
        dataframe_right.place(x=910, y=5, width=400, height=350)

        buttonframe = Frame(self.root, bd=10, padx=20, relief=RIDGE)
        buttonframe.place(x=0, y=540, width=1350, height=70)

        detailsframe = Frame(self.root, bd=10, padx=20, relief=RIDGE)
        detailsframe.place(x=0, y=620, width=1350, height=190)

        # *****************************************LABLE & ENTRY****************************************************
        lableid = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Patient Id", padx=2)
        lableid.grid(row=0, column=0, sticky=W)

        id_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.pid)
        id_enty.grid(row=0, column=1)

        lablename = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Patient Name", padx=2, pady=7)
        lablename.grid(row=1, column=0, sticky=W)
        name_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.pname)
        name_enty.grid(row=1, column=1)

        lableage = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Patient Age", padx=2, pady=7)
        lableage.grid(row=2, column=0, sticky=W)
        age_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.page)
        age_enty.grid(row=2, column=1)

        lablegender = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Patient Gender", padx=2, pady=7)
        lablegender.grid(row=3, column=0, sticky=W)
        combName = ttk.Combobox(dataframe_left, state="readonl",
                                font=("arial", 12, "bold"), width=30, textvariable=self.pgender)
        combName['value'] = ("--Select--", "Male", "Female", "Other")
        combName.current(0)
        combName.grid(row=3, column=1)

        lableaddress = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Patient Address", padx=2, pady=7)
        lableaddress.grid(row=4, column=0, sticky=W)

        address_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.paddres)
        address_enty.grid(row=4, column=1)

        labledate = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Date of Birth", padx=2, pady=7)
        labledate.grid(row=5, column=0, sticky=W)

        date_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.pdob)
        date_enty.grid(row=5, column=1)

        lableappdate = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Appointment Date", padx=2, pady=7)
        lableappdate.grid(row=6, column=0, sticky=W)

        app_date_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.adate)
        app_date_enty.grid(row=6, column=1)

        lableblood = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Patient Blood Group", padx=2, pady=7)
        lableblood.grid(row=7, column=0, sticky=W)

        blood_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.pbgpr)
        blood_enty.grid(row=7, column=1)

        labledoc = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Doctor Name", padx=2, pady=10)
        labledoc.grid(row=0, column=2, sticky=W)

        doc_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.dname)
        doc_enty.grid(row=0, column=3)

        labledocid = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Doctor Id", padx=2, pady=10)
        labledocid.grid(row=1, column=2, sticky=W)

        docid_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.did)
        docid_enty.grid(row=1, column=3)

        lableward = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Ward Name", padx=2, pady=10)
        lableward.grid(row=2, column=2, sticky=W)

        ward = Entry(dataframe_left, font=("arial", 12, "bold"),
                     width=30, textvariable=self.warno)
        ward.grid(row=2, column=3)

        lableroom = Label(dataframe_left, font=(
            "arial", 12, "bold"), text="Room No", padx=2, pady=10)
        lableroom.grid(row=3, column=2, sticky=W)
        room_enty = Entry(dataframe_left, font=(
            "arial", 12, "bold"), width=30, textvariable=self.rmno)
        room_enty.grid(row=3, column=3)

        #  **********************************************PRESCRIPTION AREA************************************
        self.txtPrescription = Text(dataframe_right, font=(
            "Time New Roma", 12, "bold"), width=40, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

       #  ***********************************************BUTTON************************************************
        btnprescription = Button(buttonframe, command=self.iprescription, text="Prescripton",
                                 bg="green", fg="white", font=("Time New Roma", 12, "bold"), width=20, height=2)
        btnprescription.grid(row=0, column=0)

        btnpresdate = Button(buttonframe, command=self.iprescriptionData, text="Insert into DataBase", font=(
            "Time New Roma", 12, "bold"), bg="green", fg="White", width=20, height=2)
        btnpresdate.grid(row=0, column=1)

        btndelete = Button(buttonframe, command=self.delete, text="Delete", font=(
            "Time New Roma", 12, "bold"), bg="green", fg="White", width=20, height=2)
        btndelete.grid(row=0, column=2)

        btnupdate = Button(buttonframe, command=self.update, text="Update", font=(
            "Time New Roma", 12, "bold"), bg="green", fg="White", width=20, height=2)
        btnupdate.grid(row=0, column=3)

        btnreset = Button(buttonframe, command=self.clear, text="Clear", font=(
            "Time New Roma", 12, "bold"), bg="green", fg="White", width=20, height=2)
        btnreset.grid(row=0, column=4)

        btnexit = Button(buttonframe, command=self.exit, text="Exit", font=(
            "Time New Roma", 12, "bold"), bg="green", fg="White", width=20, height=2)
        btnexit.grid(row=0, column=5)

        # ********************************************SCROLL BAR***********************************************
        scroll_x = ttk.Scrollbar(detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(detailsframe, column=("pid", "pname", "page", "pgender", "paddress", "pdob", "adate", "pbgrp", "dname", "did", "warno", "rmno"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("pid", text="Patient id")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("page", text="Patient Age")
        self.hospital_table.heading("pgender", text="Patient Gender")
        self.hospital_table.heading("paddress", text="Patient Address")
        self.hospital_table.heading("pdob", text="Patient DOB")
        self.hospital_table.heading("adate", text="Appointment Date")
        self.hospital_table.heading("pbgrp", text="Blood Group")
        self.hospital_table.heading("dname", text="Doctor Name")
        self.hospital_table.heading("did", text="Doctor Id")
        self.hospital_table.heading("warno", text="Ward No")
        self.hospital_table.heading("rmno", text="Room no")

        self.hospital_table.column("pid", width=95)
        self.hospital_table.column("pname", width=95)
        self.hospital_table.column("page", width=95)
        self.hospital_table.column("pgender", width=95)
        self.hospital_table.column("paddress", width=95)
        self.hospital_table.column("pdob", width=95)
        self.hospital_table.column("adate", width=98)
        self.hospital_table.column("pbgrp", width=94)
        self.hospital_table.column("dname", width=94)
        self.hospital_table.column("did", width=94)
        self.hospital_table.column("warno", width=94)
        self.hospital_table.column("rmno", width=94)

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        # self.fatch_data()

    # ***********************************************DATABASE******************************************************
    def iprescriptionData(self):
        if self.pid.get() == "":
            messagebox.showerror("Error", "All Fileds is not Fill")
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hospital_management")
            mycursor = mydb.cursor()
            mycursor.execute("insert into record values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.pid.get(), self.pname.get(), self.page.get(), self.pgender.get(),
                                                                                                self.paddres.get(), self.pdob.get(), self.adate.get(), self.pbgpr.get(),
                                                                                                self.dname.get(), self.did.get(), self.warno.get(), self.rmno.get()))
            mydb.commit()
            self.fatch_data()
            mydb.close()
            messagebox.showinfo("Success", "Record is inserted")

    # ************************************************FATCH FUN****************************************************

    def fatch_data(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital_management")
        mycursor = mydb.cursor()
        mycursor.execute("select *from record")
        rows = mycursor.fetchall()
        for i in rows:
            self.hospital_table.insert("", END, values=i)
            mydb.commit()
            mydb.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.pid.set(row[0])
        self.pname.set(row[1])
        self.page.set(row[2])
        self.pgender.set(row[3])
        self.paddres.set(row[4])
        self.pdob.set(row[5])
        self.adate.set(row[6])
        self.pbgpr.set(row[7])
        self.dname.set(row[8])
        self.did.set(row[9])
        self.warno.set(row[10])
        self.rmno.set(row[11])

    # *************************************************UPDATE FUN**************************************************

    def update(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital_management")
        mycursor = mydb.cursor()
        mycursor.execute("update record set Patient_id=%s,Patient_name=%s,Patient_age=%s,Patient_gender=%s,Patient_Address=%s,Patient_DOB=%s,Appointment_Date=%s,Patient_Blood_Group=%s,Doctor_id=%s,Doctor_name=%s,Ward_no=%s,Room_no=%s where pid=%s",
                         (self.pid.get(), self.pname.get(), self.page.get(), self.pgender.get(), self.paddres.get(), self.pdob.get(), self.adate.get(), self.pbgpr, self.dname.get(), self.did.get(), self.warno.get(), self.rmno.get()))

    # ***********************************************PRESCRIPTION FUN************************************************

    def iprescription(self):
        self.txtPrescription.insert(
            END, "Patient id:\t\t\t"+self.pid.get()+"\n")
        self.txtPrescription.insert(
            END, "Patient Name:\t\t\t"+self.pname.get()+"\n")
        self.txtPrescription.insert(
            END, "Patient Age:\t\t\t"+self.page.get()+"\n")
        self.txtPrescription.insert(
            END, "Patient Gender:\t\t\t"+self.pgender.get()+"\n")
        self.txtPrescription.insert(
            END, "Address:\t\t\t"+self.paddres.get()+"\n")
        self.txtPrescription.insert(
            END, "Date of Birth:\t\t\t"+self.pdob.get()+"\n")
        self.txtPrescription.insert(
            END, "Appointment:\t\t\t"+self.adate.get()+"\n")
        self.txtPrescription.insert(
            END, "Blood Group:\t\t\t"+self.pbgpr.get()+"\n")
        self.txtPrescription.insert(
            END, "Doctor id:\t\t\t"+self.did.get()+"\n")
        self.txtPrescription.insert(
            END, "Doctor Name:\t\t\t"+self.dname.get()+"\n")
        self.txtPrescription.insert(
            END, "Ward Name:\t\t\t"+self.warno.get()+"\n")
        self.txtPrescription.insert(
            END, "Room no:\t\t\t"+self.rmno.get()+"\n")

    # ***********************************************DELETE FUN*************************************************

    def delete(self):
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="hospital_management")
        mycursor = mydb.cursor()
        query = "delete from record where pid=%s"
        value = (self.pid.get(),)
        mycursor.execute(query, value)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "Record is Deleted")
    # **************************************************CLEAR FUN*************************************************

    def clear(self):
        self.pid.set(""),
        self.pname.set("")
        self.page.set(""),
        self.pgender.set(""),
        self.paddres.set(""),
        self.pdob.set(""),
        self.adate.set(""),
        self.pbgpr.set(""),
        self.dname.set(""),
        self.did.set(""),
        self.warno.set(""),
        self.rmno.set("")
        self.txtPrescription.delete("1.0", END)

    # **************************************************EXIT FUN*************************************************
    def exit(self):
        x = messagebox.askyesno(
            "Hospitan Mannagement System", "Do you want to exit")
        if x > 0:
            root.destroy()
            return


root = Tk()
ob = hospital(root)
root.mainloop()
