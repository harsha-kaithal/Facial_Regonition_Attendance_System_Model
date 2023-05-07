from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Model Using Python")

        #====== Variables =====
        self.var_attendance_id = StringVar()
        self.var_attendance_roll = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attendance_dept = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance_attendance = StringVar()

        # first image
        img = Image.open(r"img\attendance.jpg")
        img = img.resize((683, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=683, height=200)

        # second image
        img2 = Image.open(r"img\girl.jpeg")
        img2 = img2.resize((683, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=683, y=0, width=683, height=200)

        #back-ground img
        img4 = Image.open(r"img\face_2.jpg")
        img4 = img4.resize((1366, 500), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1366, height=500)

        title_label = Label(bg_img, text=" ATTENDANCE MANAGEMENT SYSTEM ", font=("sans-serif ", 26, "italic", "bold"), bg="white", fg="Dark blue")
        title_label.place(x=0, y=3, width=1366, height=48)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=55, width=1330, height=435)

        #left label frame

        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=5,width=645,height=420)

        img_left = Image.open(r"img\smart-attendance.jpg")
        img_left = img_left.resize((330, 100), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(Left_frame, image=self.photoimg_left)
        first_label.place(x=130, y=0, width=330, height=100)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE ,bg="white")
        left_inside_frame.place(x=5, y=105, width=629, height=287)

        #Labels and entry
        #attendance id
        attendanceID_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"),
                                bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=17, text = self.var_attendance_id , font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No.
        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                                   bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=17, text = self.var_attendance_roll, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"),
                                   bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, text = self.var_attendance_name, width=17, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

       # Department
        department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"),
                           bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        department_entry = ttk.Entry(left_inside_frame, width=17, text = self.var_attendance_dept, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"),
                           bg="white")
        date_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=17, text = self.var_attendance_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"),
                           bg="white")
        time_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=17, text = self.var_attendance_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #attendance
        attendance_label= Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white",fg="black")
        attendance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.attendance_combo_box = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), text = self.var_attendance_attendance, state="read only", width=20)
        self.attendance_combo_box["values"] = ("Status", "Present", "Absent")
        self.attendance_combo_box.current(0)
        self.attendance_combo_box.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Buttons Frame
        button_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=250, width=650, height=30)

        import_csv_button = Button(button_frame, text="Import csv", command=self.importCsv, width=16, font=("times new roman", 12, "bold"), bg="dark blue", fg="white")
        import_csv_button.grid(row=0, column=0)

        export_button = Button(button_frame, text="Export csv", command=self.exportCsv, width=16, font=("times new roman", 12, "bold"), bg="dark blue", fg="white")
        export_button.grid(row=0, column=1)

        update_button = Button(button_frame, text="Update", width=16, font=("times new roman", 12, "bold"), bg="dark blue", fg="white")
        update_button.grid(row=0, column=2)

        reset_button = Button(button_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="dark blue", fg="white")
        reset_button.grid(row=0, column=3)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=668, y=5, width=645, height=420)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=3, y=3, width=635, height=389)

        #=======: Scroll Bar Table :========
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #===========: Fetch data :==========
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fileName=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv*"),("All File","*.*")),parent=self.root)
        with open(fileName) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fileName=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv*"),("All File","*.*")),parent=self.root)
            with open(fileName,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fileName)+" successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attendance_id.set(rows[0])
        self.var_attendance_roll.set(rows[1])
        self.var_attendance_name.set(rows[2])
        self.var_attendance_dept.set(rows[3])
        self.var_attendance_time.set(rows[4])
        self.var_attendance_date.set(rows[5])
        self.var_attendance_attendance.set(rows[6])

    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_attendance_roll.set("")
        self.var_attendance_name.set("")
        self.var_attendance_dept.set("")
        self.var_attendance_time.set("")
        self.var_attendance_date.set("")
        self.var_attendance_attendance.set("")

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()

