# my calculator

from tkinter import *
root=Tk()
root.geometry('650x800')
root.title('my calculator')
#root.wm_iconbitmap('/home/vivek/Documents/GitHub/calculater_tkinter/calculater.ico')
root.configure(bg='#856ff8')
tabWidth = 4
# click function
def backspace(event):
    scvalue.set(scvalue.get()[:-1])
    screen.update()
def clear(event):
    scvalue.set('')
    screen.update()

def click(event):
    global scvalue
    text=event.widget.cget('text')

    if text=='=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value='error'
        scvalue.set(value)
        screen.update()
    elif text=='c':
        scvalue.set('')
        screen.update()
    elif text=='off':
        scvalue.set(quit())
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()



# string variable for entry widget
scvalue=StringVar()
scvalue.set('')

# making entry widget
screen=Entry(root,textvar=scvalue,font='slider 40 bold')
screen.pack(pady=10,fill=X,ipadx=9)
screen.configure(background='gray')

# first frame
f1=Frame(root,bg='#856ff8')
b1=Button(f1,text='7',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b1.pack(side=LEFT,padx=25)
b1.bind('<Button-1>',click)
b2=Button(f1,text='8',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b2.pack(side=LEFT,padx=25)
b2.bind('<Button-1>',click)
b3=Button(f1,text='9',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b3.pack(side=LEFT,padx=25)
b3.bind('<Button-1>',click)
bplus=Button(f1,text='c',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
bplus.pack(side=LEFT,padx=25)
bplus.bind('<Button-1>',click)
f1.pack(padx=12)

# second frame
f2=Frame(root,bg='#856ff8')
b4=Button(f2,text='4',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b4.pack(side=LEFT,padx=25)
b4.bind('<Button-1>',click)
b5=Button(f2,text='5',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b5.pack(side=LEFT,padx=25)
b5.bind('<Button-1>',click)
b6=Button(f2,text='6',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b6.pack(side=LEFT,padx=25)
b6.bind('<Button-1>',click)
bmiuns=Button(f2,text='-',font='slider 45 bold',relief=GROOVE,bg='gray',borderwidth=6)
bmiuns.pack(side=LEFT,padx=25)
bmiuns.bind('<Button-1>',click)
f2.pack()

# third frame
f3=Frame(root,bg='#856ff8')
b7=Button(f3,text='1',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b7.pack(side=LEFT,padx=25)
b7.bind('<Button-1>',click)
b8=Button(f3,text='2',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b8.pack(side=LEFT,padx=25)
b8.bind('<Button-1>',click)
b9=Button(f3,text='3',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b9.pack(side=LEFT,padx=25)
b9.bind('<Button-1>',click)
bmulti=Button(f3,text='*',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
bmulti.pack(side=LEFT,padx=25)
bmulti.bind('<Button-1>',click)
f3.pack()

# four frame
f4=Frame(root,bg='#856ff8')
b0=Button(f4,text='0',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
b0.pack(side=LEFT,padx=25)
b0.bind('<Button-1>',click)
bc=Button(f4,text='+',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
bc.pack(side=LEFT,padx=25)
bc.bind('<Button-1>',click)
bpercentsign=Button(f4,text='%',font='slider 35 bold',relief=GROOVE,bg='gray',borderwidth=6)
bpercentsign.pack(side=LEFT,padx=25,pady=25)
bpercentsign.bind('<Button-1>',click)
bdivide=Button(f4,text='/',font='slider 45 bold',relief=GROOVE,bg='gray',borderwidth=6)
bdivide.pack(side=LEFT,padx=25)
bdivide.bind('<Button-1>',click)
f4.pack()

# five frame
f5=Frame(root,bg='#856ff8')
bdot=Button(f5,text='.',font='slider 45 bold',relief=GROOVE,bg='gray',borderwidth=6)
bdot.pack(side=LEFT,padx=25)
bdot.bind('<Button-1>',click)
bequal=Button(f5,text='=',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
bequal.pack(side=LEFT,padx=25)
bequal.bind('<Button-1>',click)
bdouble=Button(f5,text='00',font='slider 35 bold',padx=5,pady=12,relief=GROOVE,bg='gray',borderwidth=6)
bdouble.pack(side=LEFT,padx=25)
bdouble.bind('<Button-1>',click)
boff=Button(f5,text='off',font='slider 40 bold',padx=12,pady=12,relief=GROOVE,bg='gray',borderwidth=6)
boff.pack(side=LEFT,padx=25)
boff.bind('<Button-1>',click)
f5.pack()

# six frame for clear button press and clear text 
f6=Frame(root,bg='#856ff8')
bclear=Button(f6,text='clear',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
bclear.pack(side=LEFT,padx=25,pady=5)
bclear.bind('<Button-1>',clear)
f6.pack()

# seven frame for off button press and erase one charecter backspace
f7 = Frame(root,bg='#856ff8')
bbackspace=Button(f7,text='backspace',font='slider 40 bold',relief=GROOVE,bg='gray',borderwidth=6)
bbackspace.pack(side=RIGHT,padx=2)
bbackspace.bind('<Button-1>',backspace)
f7.pack()



root.mainloop()