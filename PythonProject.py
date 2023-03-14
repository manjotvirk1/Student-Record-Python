import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import json

root=Tk()
root.configure(background="black")

#title
root.title("Student Record Keeping Application")

outer_frame=Frame(root,bg="black")
outer_frame.pack(fill=BOTH)

#explore the potential image
left_img=PhotoImage(file="explorePot.png")
left_img_label=Label(outer_frame,image=left_img,bd=0)
left_img_label.grid(row=0,column=0)

#Chitkara logo image
logo=PhotoImage(file="chitkara-university-logo.png")
logo_label=Label(outer_frame,image=logo)
logo_label.grid(row=0,column=2)

#college name
clg=Label(outer_frame,text="Chitkara University",bg="black",fg="white",font=("arial",30))
clg.grid(row=0,column=1)

heading=Label(outer_frame,text="STUDENT DATABASE",bg="black",fg="white",font=("Times New Roman",20))
heading.grid(row=1,column=1)

#main inner frame
main_frame=Frame(outer_frame,width=1000,height=450,bg="lightgrey")
main_frame.grid(row=2,column=1)

python_logo=PhotoImage(file="python_logo.gif")
python_logo_label=Label(outer_frame,image=python_logo,bd=0)
python_logo_label.grid(row=2,column=0)

end=Label(outer_frame,text="Department of Computer Science and Engineering",bg="black",fg="white",font=("Fantasy","16","bold"),pady=60)
end.grid(row=4,column=1)

# Addind tabs in main frame
tabControl=ttk.Notebook(main_frame)

tab1=Frame(tabControl)
tab2=Frame(tabControl)
tab3=Frame(tabControl)
tab4=Frame(tabControl)
tab5=Frame(tabControl)

tabControl.add(tab1,text="New Student")
tabControl.add(tab2,text="Display")
tabControl.add(tab3,text="Course Creation")
tabControl.add(tab4,text="Display Courses")
tabControl.add(tab5,text="Courses Allocation")

tabControl.pack(expand=1)

# tab1 New Student tab

#Labels for students form
name=Label(tab1,text="Enter your Name",font=15,pady=10)
roll=Label(tab1,text="Enter your RollNo",font=15,pady=10)
gender=Label(tab1,text="Choose your Gender",font=15,pady=10)
address=Label(tab1,text="Address for correspondance",font=15,pady=10)
phone=Label(tab1,text="Phone No.",font=15,pady=10)
batch=Label(tab1,text="Your Batch",font=15,pady=10)
hostel=Label(tab1,text="Hostel[Y/N]",font=15,pady=10)

name.grid(row=0,column=0)
roll.grid(row=1,column=0)
gender.grid(row=2,column=0)
address.grid(row=3,column=0)
phone.grid(row=4,column=0)
batch.grid(row=5,column=0)
hostel.grid(row=6,column=0)

namevalue=StringVar()
rollvalue=IntVar()
addressvalue=StringVar()
phonevalue=IntVar()
batchvalue=IntVar()

name_entry=Entry(tab1,width=65,textvariable=namevalue)
roll_entry=Entry(tab1,width=65,textvariable=rollvalue)

gendervalue=StringVar()
gendervalue.set(0)

male=Radiobutton(tab1,variable=gendervalue,text="Male",value="Male")
female=Radiobutton(tab1,variable=gendervalue,text="Female",value="Female")

address_entry=Entry(tab1,width=65,textvariable=addressvalue)
phone_entry=Entry(tab1,width=65,textvariable=phonevalue)

#combobox for batch
batchchoosen=ttk.Combobox(tab1,width=20,textvariable=batchvalue)
batchchoosen['values']=('2017','2018','2019','2020')

hostelvalue=IntVar()

# checkbutton for hostel facility
    
hostel_c=Checkbutton(tab1,text="Click if you need hostel facility",variable=hostelvalue)
hostel_c.grid(row=6,column=4)

#entry boxes
name_entry.grid(row=0,column=3,columnspan=2,padx=20)
roll_entry.grid(row=1,column=3,columnspan=2)
male.grid(row=2,column=3)
female.grid(row=2,column=4)
address_entry.grid(row=3,column=3,columnspan=2)
phone_entry.grid(row=4,column=3,columnspan=2)
batchchoosen.grid(row=5,column=4)


rollnos=[]

#save the record in json file
def saveas():
    global rollnos
    if os.path.isfile("student.json"):
        with open("student.json","r") as f:
            student=json.load(f)
            stu_list=student['Students']
            for i in stu_list:
                rollnos.append(i['Roll No']) 

    stu={}
    stu1={}
    stu['Students']=list()

    nameval=name_entry.get()
    rollval=rollvalue.get()

    if rollval not in rollnos:

        genderval=gendervalue.get()
        addressval=address_entry.get()
        phoneval=phonevalue.get()
        batchval=batchvalue.get()
        hostelval=True if hostelvalue==1 else False

        stu1['Roll No']=rollval
        stu1['Name']=nameval
        stu1['Gender']=genderval
        stu1['Address']=addressval
        stu1['Phone No']=phoneval
        stu1['Batch']=batchval
        stu1['Hostel']=hostelval
        
        if os.path.isfile("student.json"):
            with open("student.json","r") as f:
                stu=json.load(f)
                stu['Students'].append(stu1)
            with open("student.json","w") as f:
                json.dump(stu,f)
                
        else:
            with open("student.json","w") as f:
                stu['Students'].append(stu1)
                json.dump(stu,f)
        
        #record saved
        messagebox.showinfo("Save","Your record has been saved")

    #error for already existing roll number
    else:
        messagebox.showerror("ERROR","Your rollno already exists")

#Button to save the record
save=Button(tab1,text="Save",width=15,font=("arial",10),command=lambda:saveas())
save.grid(row=7,column=1,pady=20)


#Clear all the entries
def clearall():
    namevalue.set(""),rollvalue.set(""),gendervalue.set("0"),addressvalue.set(""),phonevalue.set(""),batchvalue.set(""),hostelvalue.set("0")

#clear all button
clear=Button(tab1,text="Clear",width=15,font=("arial",10),command=lambda:clearall())
clear.grid(row=7,column=2)


# tab2 Display
student_treeview=ttk.Treeview(tab2)

student_treeview['columns']=('roll','name','gender','address','phone','batch','hostel')
student_scroll=Scrollbar(tab2,orient="vertical", command=student_treeview.yview)
student_scroll.place(x=788, y=240, height=20+20)
student_treeview.configure(xscrollcommand=student_scroll.set)

student_treeview['show']='headings'
student_treeview.column("roll", width = 150,anchor=W)
student_treeview.column("name", width = 150,anchor=E)
student_treeview.column("gender", width = 110,anchor=W)
student_treeview.column("address", width = 110,anchor=W)
student_treeview.column("phone", width = 150,anchor=W)
student_treeview.column("batch", width = 110,anchor=W)
student_treeview.column("hostel", width = 110,anchor=E)

student_treeview.heading("roll",text="Roll No",anchor=W)
student_treeview.heading("name",text="Name",anchor=E)
student_treeview.heading("gender",text="Gender",anchor=W)
student_treeview.heading("address",text="Address",anchor=W)
student_treeview.heading("phone",text="Phone No",anchor=W)
student_treeview.heading("batch",text="Batch",anchor=W)
student_treeview.heading("hostel",text="Hostel",anchor=E)

student_treeview.pack()

#show the students record from json file
def show_stud():
    with open("student.json","r") as student_file:
        student_record=json.load(student_file)
        listOfStudents=student_record["Students"]
        for i in range(len(listOfStudents)):
            Dict= listOfStudents[i]
            student_treeview.insert(parent='',index=END, values=(Dict["Roll No"],Dict["Name"],Dict["Gender"],Dict["Address"],Dict["Phone No"],Dict["Batch"],Dict["Hostel"]))
            
        student_file.close()

#Button to show the record
show=Button(tab2,text="Show Students",bg="black",fg="white",width=20,command=lambda:show_stud())
show.pack(side=BOTTOM)


#tab3 Course Creation
for i in range(2):
    tab3.columnconfigure(i,weight=1)

course_id=StringVar()
course_name=StringVar()

courseid=Label(tab3,text="Course Id",font=("arial",10),pady=30)
courseid.grid(row=0,column=0)
courseid_entry=Entry(tab3,textvariable=course_id,width=60)
courseid_entry.grid(row=0,column=1)

coursename=Label(tab3,text="Course Name",font=("arial",10),pady=30)
coursename.grid(row=1,column=0)
coursename_entry=Entry(tab3, textvariable=course_name,width=60)
coursename_entry.grid(row=1,column=1)

# save the course in json file
def save_course():
    crs={}
    crs1={}
    crs['Courses']=list()

    crs_id=course_id.get()
    crs_name=course_name.get()

    crs1['Course ID']=crs_id
    crs1['Course Name']=crs_name
        
    if os.path.isfile("Courses.json"):
        with open("Courses.json","r") as f:
            crs=json.load(f)
            crs['Courses'].append(crs1)
        with open("Courses.json","w") as f:
            json.dump(crs,f)
            
    else:
        with open("Courses.json","w") as f:
            crs['Courses'].append(crs1)
            json.dump(crs,f)
        
    messagebox.showinfo("Save","Your record has been saved")

#save courses button
save_c=Button(tab3,text="Save",width=20,command=lambda:save_course())
save_c.grid(row=2,column=0)

#Button to clear all course enteries
def clear_course():
    course_id.set("")
    course_name.set("")

#clear courses button
clear_c=Button(tab3,text="Clear",width=20,command=lambda:clear_course())
clear_c.grid(row=2,column=1)


#tab4 Display Courses
course_treeview= ttk.Treeview(tab4)
course_treeview['columns']=("id","name")
course_scroll = Scrollbar(tab4,orient="vertical", command=course_treeview.yview)
course_scroll.place(x=780, y=240, height=20+20)
course_treeview.configure(xscrollcommand=course_scroll.set)

course_treeview['show']='headings'

course_treeview.column("id", width=200 ,anchor=W)
course_treeview.column("name", width=250,anchor=E)

course_treeview.heading("id", text="Course ID",anchor=W)
course_treeview.heading("name", text="Course Name",anchor=E)

course_treeview.pack()

#show the courses
def show_courses():
    with open("Courses.json","r") as course_file:
        course_record=json.load(course_file)
        listOfCourses=course_record["Courses"]
        for i in range(len(listOfCourses)):
            Dict= listOfCourses[i]
            course_treeview.insert(parent='',index=END, values=(Dict["Course ID"] ,Dict["Course Name"]))
        course_file.close()

#show courses button
show_c=Button(tab4, text="Show Courses",bg="black",fg="white", command=show_courses)
show_c.pack(side=BOTTOM)


#tab5 Course Allocation
for i in range(2):
    tab5.columnconfigure(i,weight=1)

rollno=StringVar()
course_al=StringVar()

rollno_label=Label(tab5,text="Student Rollno")
rollno_label.grid(row=0,column=0,pady=30)

rollno_entry=Entry(tab5,textvariable=rollno,width=60)
rollno_entry.grid(row=0,column=1)

course=Label(tab5,text="Course Name")
course.grid(row=1,column=0)

courses_values=set()
with open("Courses.json") as f:
    courses_record=json.load(f)
    course_list=courses_record["Courses"]
    for i in course_list:
        courses_values.add(i["Course Name"])

courses_combo=ttk.Combobox(tab5,width=57,state='readonly',textvariable=course_al)
courses_combo['values']=[i for i in courses_values]
courses_combo.grid(row=1,column=1)


rollnums=[]
#allocate course
def alloc():
    alloc_c={}
    alloc_c1={}
    alloc_c['Stu_Course']=list()

    rollnum=int(rollno.get())
    course_nm=course_al.get()

    with open("Courses.json","r") as stu_crs:
        course_o=json.load(stu_crs)
        course_i=course_o['Courses']

    alloc_c1['Rollno']=rollnum
    #getting valid rollno
    with open("student.json","r") as f:
        stud_rec=json.load(f)
        students=stud_rec["Students"]
        for stu_dict in students:
            rollnums.append(stu_dict["Roll No"])

    if rollnum not in rollnums:
        messagebox.showerror("Error","The Roll No does not exist")
        rollno.set("")
    

    else:
        #getting course id from course name
        for i in range(len(course_i)):
            if course_i[i]["Course Name"]==course_nm:
                alloc_c1['CourseID']=course_i[i]['Course ID']

                if os.path.isfile("Allocation.json"):
                    with open("Allocation.json","r") as f:
                        alloc_c=json.load(f)
                        alloc_c['Stu_Course'].append(alloc_c1)
                    with open("Allocation.json","w") as f:
                        json.dump(alloc_c,f)
                    
                else:
                    with open("Allocation.json","w") as f:
                        alloc_c['Stu_Course'].append(alloc_c1)
                        json.dump(alloc_c,f)

                messagebox.showinfo("Allocate","The course has been allocated")
                
         
        

allocate=Button(tab5,text="Allocate",width=20,command=lambda:alloc())
allocate.grid(row=2,column=0,columnspan=2,pady=50)

mainloop()