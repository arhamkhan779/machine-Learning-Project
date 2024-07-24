import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg
import backend as bk

bk.load_save_artifects()
class Main:
    def __init__(self,root):
        self.root=root
        self.root.title("Diabetes Prediction Desktop Application")
        self.root.resizable(0,0)
        self.root.geometry("1370x700+0+0")

        self.main_frame=Frame(self.root,background="#331E38")
        self.main_frame.pack(fill=BOTH,expand=True)

        self.main_label=Label(self.main_frame,text="Diabetes Prediction Application",font=('times new roman',50,'bold'),bd=7,relief=GROOVE,bg="#031926",foreground="lightyellow")
        self.main_label.pack(side=TOP,fill=X)

        self.main_label2=Label(self.main_frame,text="Random Forest Classifier",font=('times new roman',50,'bold'),bd=7,relief=GROOVE,bg="#031926",foreground="lightyellow")
        self.main_label2.pack(side=BOTTOM,fill=X)

        self.credentials=LabelFrame(self.main_frame,text="Input Credentials",relief=RIDGE,bd=7,bg="#331E38",fg='lightyellow')
        self.credentials.place(x=10,y=100,height=500,width=585)

        self.prediction=LabelFrame(self.main_frame,text="Prediction",relief=RIDGE,bd=7,bg="white",fg="black")
        self.prediction.place(x=600,y=100,height=500,width=585)

        self.classify_btn=Button(self.main_frame,text="Classify",font=("times new roman",20,'bold'),bd=7,relief=RIDGE,bg="#031926",fg="lightyellow",activebackground="#031926",command=self.classify)
        self.classify_btn.place(x=1190,y=100,height=250,width=163)

       
        def label(frame,text,row,col):
           lab=Label(frame,text=text,font=("times new roman",25,'bold'),fg="lightyellow",bg="#331E38")
           lab.grid(column=col,row=row,sticky=W,padx=10,pady=10)

        list=['Gender','Age','Hyper Tension',"Heart disease",'BMI','HbA1c','Blood Glucose']

        for i in range(len(list)):
            label(self.credentials,list[i],i,0)
        
        self.agee=IntVar()
        age=Entry(self.credentials,font=("times new roman",14,'bold'),bd=5,relief=RIDGE,width=30,textvariable=self.agee)
        age.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        self.hba=IntVar()
        hb=Entry(self.credentials,font=("times new roman",14,'bold'),bd=5,relief=RIDGE,width=30,textvariable=self.hba)
        hb.grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        self.bmii=IntVar()
        bmi=Entry(self.credentials,font=("times new roman",14,'bold'),bd=5,relief=RIDGE,width=30,textvariable=self.bmii)
        bmi.grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
        self.blood_glucose=IntVar()
        bg=Entry(self.credentials,font=("times new roman",14,'bold'),bd=5,relief=RIDGE,width=30,textvariable=self.blood_glucose)
        bg.grid(row=6,column=1,padx=10,pady=10,sticky=W)
        
        self.genderl=StringVar()
        self.gender=OptionMenu(self.credentials,self.genderl,'Male','Female','Others')
        self.gender.place(x=246,y=22,width=311)

        self.tension=StringVar()
        self.hyper=OptionMenu(self.credentials,self.tension,'Yes','No')
        self.hyper.place(x=246,y=143,width=311)

        self.heart_disease=StringVar()
        self.heart=OptionMenu(self.credentials,self.heart_disease,'Yes','No')
        self.heart.place(x=246,y=205,width=311)
        
        def clear():
           self.text.delete(1.0,END)
           age.delete(0,END)
           hb.delete(0,END)
           bg.delete(0,END)
           bmi.delete(0,END)

        self.clear_btn=Button(self.main_frame,text="Clear",font=("times new roman",20,'bold'),bd=7,relief=RIDGE,bg="#331E38",fg="lightyellow",activebackground="#031926",command=clear)
        self.clear_btn.place(x=1190,y=355,height=250,width=163)

        self.pt_data=Label(self.prediction,text="Patients Data",font=("times new roman",40,'bold'),bg="#031926",fg="lightyellow",bd=7,relief=GROOVE)
        self.pt_data.pack(side=TOP,fill=X)

        self.text=Text(self.prediction,font=("times new roman",18,'bold'),bg="#331E38",fg="lightyellow")
        self.text.place(x=0,y=80,width=570,height=390)

        

    def classify(self):
        diab=['Non Diabetec','Diabetec']
        if self.agee.get()==0 or self.bmii.get() == 0 or self.blood_glucose.get() == 0 or self.hba.get()==0 or self.agee.get()==" " or self.hba.get()==' ' or self.blood_glucose.get()==" " or self.bmii.get()==" " or self.genderl.get()==" ":
            msg.showerror("Zero Error","Please input some value")
        else:
            try:
                age=int(self.agee.get())
                bmi=int(self.bmii.get())
                bg=int(self.blood_glucose.get())
                hb=int(self.hba.get())
                gender=self.genderl.get()
                tension=self.tension.get()
                hd=self.heart_disease.get()
                value,prob=bk.classify(gender,age,tension,hd,bmi,hb,bg)
                
                value=diab[value[0]]
                non_diabetec=prob[0][0]
                diabetec=prob[0][1]
                
                self.text.insert(1.0,f"The Person Having Following Health Conditions\n\nGender:{gender}\nAge:{age}\nhyper Tension:{tension}\nHeart Disease:{hd}\nBMI:{bmi}\nHbA1c:{hb}\nBlood Glucose:{bg}\n\n is declared as {value}\n\nDiabetec Probability:{diabetec}\nNon Diabetec Probability:{non_diabetec}")
            except ValueError:
                msg.showerror("Wrong Value","Please inout Numeric values")
 

if __name__ == "__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()