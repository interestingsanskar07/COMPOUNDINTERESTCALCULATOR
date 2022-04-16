from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Initial Principal Balance')
        self.lbl2=Label(win, text='Interest Rate')
        self.lbl3=Label(win,text='COMPOUND INTREREST AMOUNT')
        self.lbl4=Label(win, text='Number of Time periods elapased(in years)')
        self.lbl5=Label(win, text='Final Amount')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.t6 = Entry(win ,width = 300)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=400, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=400, y=100)
        self.lbl4.place(x=100, y=150)
        self.t4.place(x=400, y=150)
        self.btn1 = Button(win, text='SHOW RESULT')
        self.b1=Button(win, text='SHOW RESULT', command=self.compound)
        self.b1.place(x=150, y=300)
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=400, y=250)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=400, y=200)
        self.t5.place(x=50, y=350)

    def compound(self):
        self.t5.delete(0,'end')
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        num4 = int(self.t4.get())
        result = num1 * (pow((1 + num2/100),num4))
        result1 = result - num1
        if(num2>18):
            result2 = 'INTEREST RATE IS VERY HIGH COMPARATIVELY'
        if(num4>10):
            result2 = 'FOR TOO MANY YEARS YOU HAVE BEEN ON LOAN'
        else:
            result2 = 'KEEP IT UP AND YAAD SE INTEREST BHARTE CHALO'
        self.t5.insert(END,str(result))
        self.t3.insert(END,str(result1))
        self.t5.insert(END,str(result2))
window=Tk()
mywin=MyWindow(window)
window.title('COMPOUND INTEREST CALCULATOR')
window.geometry("600x600+10+10")
window.mainloop()