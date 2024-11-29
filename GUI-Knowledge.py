from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI=Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('800x500')#ขนาดโปรแกรม


L1=Label(GUI,text='โปรแกรมบันทึกการใช้จ่าย',font=('Angsana New',20),fg='green')
L1.place(x=10,y=10)


####################################
def Button2():
    text='ตอนนี้มีเงินในบัญชีอยู่ 5000 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1=LabelFrame(GUI,text='รายรับ')#คล้ายกระดาน
FB1.place(x=50,y=50)
B2=ttk.Button(FB1,text='เงินทั้งหมด',command=Button2)
B2.pack(ipadx=20,ipady=20,padx=5,pady=5)
####################################


def Button3():
    text='สัปดาห์นี้้เติมน้ำมัน500'
    messagebox.showinfo('เงินเติมน้ำมัน',text)

FB2=LabelFrame(GUI,text='ใช้จ่าย')#คล้ายกระดาน
FB2.place(x=250,y=50)
B3=ttk.Button(FB2,text='แบ่งเงินใช้จ่าย',command=Button3)
B3.pack(ipadx=20,ipady=20,padx=5,pady=5)
######################################

def Button4():
    text='เดือนนี้เก็บเพิ่่ม 17%'
    messagebox.showinfo('กบข',text)

FB3=LabelFrame(GUI,text='เงินเก็บ')#คล้ายกระดาน
FB3.place(x=450,y=50)
B4=ttk.Button(FB3,text='เก็บใน กบข.',command=Button4)
B4.pack(ipadx=20,ipady=20,padx=5,pady=5)


##########################################

def Button5():
    text='ซื้อ DOGE เพิ่ม 1000 บาท'
    messagebox.showinfo('bitcub',text)

B5=ttk.Button(FB3,text='เก็บในDOGE',command=Button5)
B5.pack(ipadx=20,ipady=20,padx=5,pady=5)
#########################################
def Button6():
    text='เงินสด 5000'
    messagebox.showinfo('บัญชีเงินเก็บ',text)

B6=ttk.Button(FB3,text='cash',command=Button6)
B6.pack(ipadx=20,ipady=20,padx=5,pady=5)

GUI.mainloop()
