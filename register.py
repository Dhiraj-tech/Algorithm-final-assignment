from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connection import *
from Gui import *

class Register:
    def __init__(self):
        self.mainsc()
        self.database=DataBase()
        self.gui_main=Airline()

    def reg(self):
        try:
            self.window=Tk()
            self.window.title('New registration')
            self.window.geometry('800x600')
            self.window.configure(bg='light blue')
            self.lbl = Label(self.window, text='Enter first name')
            self.lbl.place(x=300,y=50)
            self.ent_name = Entry(self.window)
            self.ent_name.place(x=400, y=50)
            self.lbl = Label(self.window, text='Enter last name')
            self.lbl.place(x=300, y=100)
            self.ent_ls = Entry(self.window)
            self.ent_ls.place(x=400, y=100)
            self.lbl = Label(self.window, text='Address')
            self.lbl.place(x=300, y=150)
            self.ent_ad = Entry(self.window)
            self.ent_ad.place(x=400, y=150)
            self.lbl = Label(self.window, text='Username')
            self.lbl.place(x=300, y=250)
            self.ent_un = Entry(self.window)
            self.ent_un.place(x=400, y=250)
            self.lbl =Label(self.window, text='Contact no:')
            self.lbl.place(x=300, y=200)
            self.ent_pn = Entry(self.window)
            self.ent_pn.place(x=400, y=200)
            self.lbl = Label(self.window, text='Password')
            self.lbl.place(x=300,y=300)
            self.ent_ps = Entry(self.window)
            self.ent_ps.place(x=400, y=300)
            self.but = Button(self.window,text="Register ", command=self.getting)
            self.but.place(x=390,y=400)
            self.window.mainloop()

        except Exception as e:
            print(e)

    def getting(self):
        try:
            self.database = DataBase()
            first_name = self.ent_name.get()
            last_name = self.ent_ls.get()
            username = self.ent_un.get()
            password = self.ent_ps.get()
            phone = self.ent_pn.get()
            address = self.ent_ad.get()
            if first_name == '' or last_name == '' or username == '' or password == '' or phone == '' or address == '':
                messagebox.showerror('Error', ' Enter each boxes carefully!')

            else:
                qry = "SELECT username from user_reg order by username"
                data = self.database.get_data(qry)
                tup = self.algo_search(data, username)
                print(tup)
                if tup != -1:
                    messagebox.showerror('Try Again!', 'Username already taken!')
                    return False

                else:
                    qry = '''insert into user_reg (username,password,first_name,last_name,address,phone) values(%s,%s,%s,%s,%s,%s)'''
                    values = (username, password, first_name, last_name, address, phone)
                    self.database.iud(qry, values)
                    messagebox.showinfo('Done', ' Registered successfully!')
                    return True
        except Exception as e:
            print(e)


    def login(self):
        try:
            self.window1 = Tk()
            self.window1.title(' login')
            self.window1.geometry('600x400')
            self.window1.configure(bg='light blue')
            self.username = Label(self.window1,text = ' Username ')
            self.username.place(x=50, y=20)
            self.un_ent = Entry(self.window1)
            self.un_ent.place(x=130, y=20)
            self.password = Label(self.window1, text=' Password ')
            self.password.place(x=50, y=60)
            self.ps_ent = Entry(self.window1)
            self.ps_ent.place(x=130, y=60)
            self.but1 = Button(self.window1, text="login here", command=self.login_backend)
            self.but1.place(x=105, y=100)
            self.window1.mainloop()
        except Exception as e:
            print(e)

    def login_backend(self):
        try:
            self.database = DataBase()
            self.gui_main = Airline()
            userna =self.un_ent.get()
            passw =self.ps_ent.get()
            if userna=='' or passw=='':
                messagebox.showerror("error","enter username or password first!")
            else:
                qry='''select * from user_reg where username=%s and password=%s'''
                values=(userna,passw)
                get_dt=self.database.get_data_p(qry,values)

                if len(get_dt)==1:
                    messagebox.showinfo("Login successfull")
                    self.gui_main.main()
                else:
                    messagebox.showerror("Error","Wrong password or username")
        except Exception as e:
            print(e)

    def mainsc(self):
        try:
            self.window2=Tk()
            self.window2.title('Airline Ticket Booking system')
            self.window2.geometry('600x400')
            self.lbl= Label(text="Choose Login Or Register", bg="orange", width="300", height="2", font=("Calibri", 13)).pack()
            self.lbl= Label(text="").pack()
            self.but = Button(self.window2, text="REGISTER", command=self.reg, bg='light green', height="2",width="30" ,font="Bold 10")
            self.but.pack()
            self.but = Button(self.window2, text="LOGIN", command=self.login, bg='light green', height="2",width="30", font="bold 10")
            self.but.pack(padx=10,pady=10)
            self.window2.mainloop()
        except Exception as e:
            print(e)

    def algo_search(self, list, key):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][0] == key:

                return mid

            elif list[mid][0] > key:
                end = mid - 1

            else:
                start = mid + 1

        return -1


Register()