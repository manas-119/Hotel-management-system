import tkinter as tk
from tkinter import messagebox as mb
r=tk.Tk()
r.attributes('-fullscreen',True)
r_id=tk.StringVar()
c_name=tk.StringVar()
c_ph=tk.StringVar()
t_mems=tk.StringVar()
t_days=tk.StringVar()

title_l=tk.Label(r,text='HOTEL MANAGEMENT',font="sans 15 bold")
title_l.pack(side='top')

new_l=tk.Label(r,text='NEW CUSTOMER',font="sans 12 bold")
new_l.place(x=250,y=80)

r_l=tk.Label(r,text='ROOM_ID',font="sans 9 bold")
r_l.place(x=220,y=110)
r_e=tk.Entry(r,font="sans 9 bold",textvariable=r_id,width=20)
r_e.place(x=300,y=110)


n_l=tk.Label(r,text='NAME',font="sans 9 bold")
n_l.place(x=220,y=140)
n_e=tk.Entry(r,textvariable=c_name,width=20,font="sans 9 bold")
n_e.place(x=300,y=140)


P_l=tk.Label(r,text='PHONE',font="sans 9 bold")
P_l.place(x=220,y=170)
p_e=tk.Entry(r,textvariable=c_ph,width=20,font="sans 9 bold")
p_e.place(x=300,y=170)


d_l=tk.Label(r,text='DAYS',font="sans 9 bold")
d_l.place(x=220,y=200)
d_e=tk.Entry(r,textvariable=t_days,width=20,font="sans 9 bold")
d_e.place(x=300,y=200)


m_l=tk.Label(r,text='MEMS',font="sans 9 bold")
m_l.place(x=220,y=230)
m_e=tk.Entry(r,textvariable=t_mems,width=20,font="sans 9 bold")
m_e.place(x=300,y=230)

def submit():
    room=r_e.get()
    uname=n_e.get()
    uphone=p_e.get()
    ndays=d_e.get()
    nmems=m_e.get()
    if(len(uname)>=3 and len(uphone)==10 and int(nmems)<=5 and int(ndays)>0):
        try:
            import mysql.connector as mc
            con=mc.connect(host='localhost',user='root',passwd='abc@123',database='hotel')
            cur=con.cursor()
            Q='insert into demo(room_id,name,phone,days_be,mems) values(%s,%s,%s,%s,%s)'
            val=(room,uname,uphone,ndays,nmems)
            cur.execute(Q,val)
            con.commit()
            mb.showinfo('OKAY','ROOM ALLOCATED ')
        except Exception as e:
            mb.showerror('FALSE',e)
    else:
        mb.showerror('FALSE','INVALID DATA')
    r_id.set('')
    c_name.set('')
    c_ph.set('')
    t_days.set('')
    t_mems.set('')
    


    
b=tk.Button(r,text='ALLOCATE',command=submit,font="sans 10 bold")
b.place(x=300,y=260)
####INSERT OVER

###DELETE BEGIN

vec_l=tk.Label(r,text='EXIT',font="sans 12 bold")
vec_l.place(x=300,y=440)


vec_r_l=tk.Label(r,text='ROOM ID',font="sans 9 bold")
vec_r_l.place(x=230,y=470)

v_r_id=tk.StringVar()
v_r_e=tk.Entry(r,textvariable=v_r_id,width=17,font="sans 12 bold")
v_r_e.place(x=300,y=470)


def vac_me():
    v_room_id=v_r_id.get()
    try:
        import mysql.connector as mc
        con=mc.connect(host='localhost',user='root',passwd='abc@123',database='hotel')
        cur=con.cursor()
        Q='select room_id from demo'
        cur.execute(Q)
        room_list=[]
        for i in cur:
            room_list.append(i[0])
        con.commit()
#       print(room_list)
        if(int(v_room_id) in room_list):
            try:
                import mysql.connector as mc
                con=mc.connect(host='localhost',user='root',passwd='abc@123',database='hotel')
                cur=con.cursor()
                Q="delete from demo where room_id='"+v_room_id+"'"
                cur.execute(Q)         
                con.commit()
                mb.showinfo('DONE',"Room no "+str(v_room_id)+' is Vecated')

            except Exception as e:
                mb.showerror('FALSE',e)
        else:
            mb.showerror('FALSE','not found')
    except Exception as e:
        mb.showerror('FALSE',e)
    v_r_id.set('')
close=tk.Button(r,text='DELETE',command=vac_me,font="sans 10 bold")
close.place(x=300,y=500)

###DELETE OVER

cal_r_l=tk.Label(r,text='GENERATE BILL',font="sans 12 bold")
cal_r_l.place(x=800,y=245)

cal_r_l=tk.Label(r,text='ROOM ID',font="sans 9 bold")
cal_r_l.place(x=800,y=270)

cal_r_id=tk.StringVar()
cal_r_e=tk.Entry(r,textvariable=cal_r_id,width=17,font="sans 12 bold")
cal_r_e.place(x=880,y=270)


def bill():
    try:
        bill_id=cal_r_id.get()

        import mysql.connector as mc
        con=mc.connect(host='localhost',user='root',passwd='abc@123',database='hotel')
        cur=con.cursor()
        Q='select room_id from demo'
        cur.execute(Q)
        room_list=[]
        for i in cur:
            room_list.append(i[0])
        con.commit()
        print(room_list)
        if bill_id !="" and int(bill_id) in room_list:
            import mysql.connector as mc
            con=mc.connect(host='localhost',user='root',passwd='abc@123',database='hotel')
            cur=con.cursor()
            Q="select name,phone,days_be,mems from demo where room_id='"+bill_id+"'"
            cur.execute(Q)
            l=[]
            for i in cur:
                l.append(i)
            NAME=l[0][0]
            PHONE=l[0][1]
            DAYS=int(l[0][2])
            TBILL=DAYS*750
            MEMS=l[0][3]
            con.commit()
            try:
                f=open('----------------------TOTAL BILL-------------------.txt','w')
                total="\n\n\n NAME:  "+NAME+" \n PHONE :  "+str(PHONE)+" \n  ROOM NO :  "+str(bill_id)+" \n DAYS SPEND :  "+str(DAYS)+" \n TOTAL MEMBERS : "+str(MEMS)+"\n ------------------------------------------ \n TOTAL BILL ----------------->"+str(TBILL)
                f.write(total)
                f.close()
                if(len(total)>0):
                    import os
                    os.startfile('----------------------TOTAL BILL-------------------.txt','print')
                else:
                    mb.showinfo('Sorry!!','cant generate your bill')
                mb.showinfo('Done','Thank You!!!')
            except Exception as e:
                mb.showerror('FALSE',e)
            
        else:
            mb.showerror('FALSE','ENTER PROPER ROOM ID')
        cal_r_id.set('')
    except Exception as e:
        mb.showerror('FALSE',e)
close=tk.Button(r,text='BILL',command=bill,font="sans 10 bold")
close.place(x=1045,y=270)



###filled
def cntroom():
    try:
        import mysql.connector as mc
        con=mc.connect(host='localhost',user='root',passwd='abc@123',database='hotel')
        cur=con.cursor()
        Q="select count(*) from demo"
        cur.execute(Q)
        x=""
        for i in cur:
            x=x+str(i[0])
        if int(x)==0:
            mb.showinfo('FALSE','NOT YET ALLOTED ANY ROOM')
        else:    
            mb.showinfo('FILLED',str(x)+" rooms are filled")
        con.commit()
    except Exception as e:
        mb.showerror('False',e)
cnt=tk.Button(r,text='TOTAL ',command=cntroom,font="sans 9 bold")
cnt.place(x=1250,y=10)
###filled close

###busy
def busyroom():
    try:
        import mysql.connector as mc
        con=mc.connect(host='localhost',user='root',passwd='abc@123',database='hotel')
        cur=con.cursor()
        Q="select room_id from demo"
        cur.execute(Q)
        x=""
        for i in cur:
            x=x+str(i[0])+'\n'
        con.commit()
        if len(x)>0:
            txt=tk.Text(r,width=25,heigh=2,font="sans 10 bold")
            txt.place(x=1050,y=35)
            txt.insert(tk.END,x)
            def QIT():
                cross.place_forget()
                txt.place_forget()
            cross=tk.Button(r,bd=1,text="X",command=QIT,font="sans 10 bold",bg="red")
            cross.place(x=1030,y=35)
        else:
            mb.showinfo('FALSE','NOT YET ALLOTED ANY ROOM')
        
    except Exception as e:
        mb.showerror('False',e)
busy=tk.Button(r,text='CURRENTLY BUSY',command=busyroom,font="sans 9 bold")
busy.place(x=1050,y=10)
###busy close


###close
def quit_me():
    r.destroy()
close=tk.Button(r,text='X',command=quit_me,font="sans 9 bold",bg='red')
close.place(x=1325,y=10)

r.mainloop()
