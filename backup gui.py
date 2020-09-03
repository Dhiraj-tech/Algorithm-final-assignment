from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connection import *
from datetime import *

from connection import DataBase


class Airline():
    def __init__(self):
        self.database = DataBase()
        self.index = ""

    def main(self):
        try:
            self.search = SearchFlight()
            self.root = Tk()
            self.root.withdraw()
            self.wn = Toplevel(self.root)
            self.wn.protocol("WM_DELETE_WINDOW", self.wn.destroy)
            self.wn.title("Airline Ticket Booking System")
            self.wn.geometry("515x500")
            self.wn.configure(bg="light blue")
            self.lbl = Label(self.wn, text="Select Your Choice", bg="orange", width="300", height="2",
                             font=("Bold", 15)).pack()
            self.btn = Button(self.wn, text="Register flight", width=30, font="Bold 10", bg="light green", fg="black",
                              command=self.register_flight)
            self.btn.pack()
            self.btn1 = Button(self.wn, text="Search the Flight", width=30, font="Bold 10", bg="light green", fg="black",
                               command=self.search.searchgui)
            self.btn1.pack(padx=10, pady=10)
            self.root.mainloop()
        except Exception as e:
            print(e)

    def register_flight(self):
        try:
            self.wn.destroy()
            global wn1
            self.wn1 = Toplevel()
            self.wn1.title("Welcome customer to  Roy Airlines Booking")
            self.wn1.geometry("1300x380")
            self.wn1.configure(bg="light blue")

            self.lbl = Label(self.wn1, text="Airline company: ", fg="dark blue", width=15,
                             font=("arial", 12, "bold"))
            self.lbl.grid(row=0, column=0)
            self.entry_ac = Entry(self.wn1, width=35)
            self.entry_ac.grid(row=0, column=1)

            self.p = Label(self.wn1, text="Plane model: ", fg="dark blue", width=15,
                           font=("arial", 12, "bold"))
            self.p.grid(row=1, column=0)
            self.entry_p = Entry(self.wn1, width=35)
            self.entry_p.grid(row=1, column=1)

            self.combo = ["Ktm to Birjung", "Birgunj to Ktm", "Nepalgunj to Pokhara", "Palpa to Kathmandu",
                          "Pokhara to KTM ", "Chitwan to KTM", "Janakpur to KTM"]
            self.b = Label(self.wn1, text=" Plane Route: ", fg="dark blue", width=15, font=("arial", 12, "bold"))
            self.b.grid(row=2, column=0)
            self.combox = ttk.Combobox(self.wn1, values=self.combo, width=30)
            self.combox.set("Route")
            self.combox.grid(row=2, column=1)

            self.tc = Label(self.wn1, text="Ticket price ", fg="dark blue", width=15, font=("arial", 12, "bold"))
            self.tc.grid(row=6, column=0)
            self.entry_tc = Entry(self.wn1, width=35)
            self.entry_tc.grid(row=6, column=1)

            self.Ph = Label(self.wn1, text="No. of seats: ", fg="dark blue", width=15, font=("arial", 12, "bold"))
            self.Ph.grid(row=7, column=0)
            self.entry_st = Entry(self.wn1, width=35)
            self.entry_st.grid(row=7, column=1)

            self.des = Label(self.wn1, text="Description: ", fg="dark blue", width=15,
                             font=("arial", 12, "bold"))
            self.des.grid(row=9, column=0)
            self.entry_des = Entry(self.wn1, width=35)
            self.entry_des.grid(row=9, column=1)

            self.view_tree = ttk.Treeview(self.wn1, column=('a', 'b', 'c', 'd', 'f', 'g'))
            self.view_tree.place(x=550, y=80)
            self.view_tree['show'] = 'headings'
            self.view_tree.column('a', width=100)
            self.view_tree.column('b', width=100)
            self.view_tree.column('c', width=200)
            self.view_tree.column('d', width=70)
            self.view_tree.column('f', width=70)
            self.view_tree.column('g', width=150)
            self.view_tree.heading('a', text='Company')
            self.view_tree.heading('b', text='Model no.')
            self.view_tree.heading('c', text='Route')
            self.view_tree.heading('d', text='Ticket Price')
            self.view_tree.heading('f', text='Total seat')
            self.view_tree.heading('g', text='Description')
            self.for_treeview()

            self.upd = Button(self.wn1, text="Add", width=10, height=1, font=("arial", 12, "bold"),
                              fg="black", command=self.register_plane)
            self.upd.place(x=60, y=300)

            self.hm = Button(self.wn1, text="Update", width=10, height=1, font=("arial", 12, "bold"),
                             fg="black", command=self.update_item)
            self.hm.place(x=170, y=300)

            self.cancl = Button(self.wn1, text="Delete", width=10, height=1,
                                font=("arial", 12, "bold"), fg="black", command=self.delete_item)
            self.cancl.place(x=280, y=300)

            self.ext = Button(self.wn1, text="Exit", command=self.wn1.quit, bg='red')
            self.ext.place(x=1200, y=340)
        except Exception as e:
            print(e)

    def register_plane(self):
        try:
            company = self.entry_ac.get()
            model = self.entry_p.get()
            route = self.combox.get()
            price = self.entry_tc.get()
            seat = self.entry_st.get()
            des = self.entry_des.get()

            if company == "" or model == '' or route == '' or price == '' or seat == '' or des == '':
                messagebox.showerror('Error', "Fill up all the entries")

            else:
                self.add_plane()
                messagebox.showinfo('Done', 'Registered successfully!')
                self.for_treeview()
        except Exception as e:
            print(e)

    def add_plane(self):
        try:
            self.database = DataBase()
            company = self.entry_ac.get()
            model = self.entry_p.get()
            route = self.combox.get()
            price = self.entry_tc.get()
            seat = self.entry_st.get()
            des = self.entry_des.get()

            qry = '''insert into plane_reg (company, model, route, price, seat, des) values (%s,%s,%s,%s,%s,%s)'''
            vals = (company, model, route, price, seat, des)
            ohoni = self.database.iud(qry, vals)
            print(ohoni)
        except Exception as e:
            print(e)

    def for_treeview(self):
        try:
            qry = 'select * from plane_reg'
            output = self.database.get_data(qry)
            self.view_tree.delete(*self.view_tree.get_children())
            for i in output:
                self.view_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
            self.view_tree.bind("<Double-1>", self.select_plane)
        except Exception as e:
            print(e)

    def select_plane(self, event):
        try:
            sel_row = self.view_tree.selection()[0]
            sel_item = self.view_tree.item(sel_row)
            self.index = self.view_tree.item(sel_row, 'text')
            selected_data = self.view_tree.item(sel_row, 'values')
            self.entry_ac.delete(0, 'end')
            self.entry_ac.insert(0, selected_data[0])
            self.entry_p.delete(0, 'end')
            self.entry_p.insert(0, selected_data[1])
            self.combox.delete(0, 'end')
            self.combox.insert(0, selected_data[2])
            self.entry_tc.delete(0, 'end')
            self.entry_tc.insert(0, selected_data[3])
            self.entry_st.delete(0, 'end')
            self.entry_st.insert(0, selected_data[4])
            self.entry_des.delete(0, 'end')
            self.entry_des.insert(0, selected_data[5])
        except Exception as e:
            print(e)

    def update_plane(self, index, company, model, route, price, seat, des):
        try:
            self.database = DataBase()
            qry = "UPDATE plane_reg SET company = %s, model = %s, route = %s, price=%s, seat=%s, des =%s  WHERE id = %s"
            values = (company, model, route, price, seat, des, index)
            self.database.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def update_item(self):
        try:
            self.database = DataBase()
            company = self.entry_ac.get()
            model = self.entry_p.get()
            route = self.combox.get()
            price = self.entry_tc.get()
            seat = self.entry_st.get()
            des = self.entry_des.get()

            if self.index == "":
                messagebox.showerror("Error", "Select Item first")
            elif not company == "" or model == '' or route == '' or price == '' or seat == '' or des == '':

                if self.update_plane(int(self.index), company, model, route, price, seat, des):
                    messagebox.showinfo("Item", "Item Updated")
                    self.for_treeview()
                    print(self.index)
                else:
                    messagebox.showerror("Error", "Item can not be Updated")
        except Exception as e:
            print(e)

    def delete_item(self):
        self.database = DataBase()
        try:
            if self.index == "":
                messagebox.showerror("Error", "Select Item first")
                return False

            else:
                qry = "DELETE FROM plane_reg  WHERE id=%s"
                values = ([self.index])
                self.database.iud(qry, values)
                messagebox.showinfo("Done", "Plane removed")
                self.for_treeview()
                print(self.index)
                return True

        except Exception as e:
            print(e)


class SearchFlight:
    def __init__(self):
        self.database = DataBase()

    def searchgui(self):

        try:
                self.wn1 = Toplevel()
                self.wn1.title("Welcome customer to our Searching the Flight")
                self.wn1.geometry("1300x380")
                self.wn1.configure(bg="light green")

                self.lbl = Label(self.wn1, text="Sort by ", fg="dark blue",
                                 font=("arial", 10, "bold"))
                self.lbl.place(x=30, y=30)
                como = ["Route", 'Company', 'Price']
                self.entry = ttk.Combobox(self.wn1, values=como)
                self.entry.set('---sortby----')
                self.entry.place(x=100, y=30)

                self.lbl1 = Label(self.wn1, text="Keyword ", fg="dark blue",
                                  font=("arial", 10, "bold"))
                self.lbl1.place(x=30, y=70)
                self.entry2 = Entry(self.wn1)
                self.entry2.place(x=100, y=70)

                self.sc_but = Button(self.wn1, text="Search", command=self.search_button, font=("arial", 10, "bold"))
                self.sc_but.place(x=170, y=100)

                self.lbl = Label(self.wn1, text="Company: ", fg="dark blue", width=15,
                                 font=("arial", 10, "bold"))
                self.lbl.place(x=30, y=160)
                self.entry_ac = Entry(self.wn1,textvariable='a')
                self.entry_ac.place(x=190, y=160)

                self.p = Label(self.wn1, text="Plane model: ", fg="dark blue", width=15,
                               font=("arial", 10, "bold"))
                self.p.place(x=30, y=190)
                self.entry_p = Entry(self.wn1)
                self.entry_p.place(x=190, y=190)

                self.b = Label(self.wn1, text=" Plane Route: ", fg="dark blue", width=15, font=("arial", 10, "bold"))
                self.b.place(x=30, y=220)
                self.combox = Entry(self.wn1, width=30,textvariable='b')
                self.combox.place(x=190, y=220)

                self.tc = Label(self.wn1, text="Ticket price ", fg="dark blue", font=("arial", 10, "bold"))
                self.tc.place(x=70, y=250)
                self.entry_tc = Entry(self.wn1,textvariable='c')
                self.entry_tc.place(x=190, y=250)

                self.Ph = Label(self.wn1, text="No. of seats: ", fg="dark blue", font=("arial", 10, "bold"))
                self.Ph.place(x=70, y=280)
                self.entry_st = Entry(self.wn1, width=35)
                self.entry_st.place(x=190, y=280)

                self.des = Label(self.wn1, text="Description: ", fg="dark blue",
                                 font=("arial", 10, "bold"))
                self.des.place(x=70, y=310)
                self.entry_des = Entry(self.wn1, width=35)
                self.entry_des.place(x=190, y=310)

                self.view_tree = ttk.Treeview(self.wn1, column=('a', 'b', 'c', 'd', 'f', 'g'))
                self.view_tree.place(x=550, y=80)
                self.view_tree['show'] = 'headings'
                self.view_tree.column('a', width=100)
                self.view_tree.column('b', width=100)
                self.view_tree.column('c', width=200)
                self.view_tree.column('d', width=70)
                self.view_tree.column('f', width=70)
                self.view_tree.column('g', width=150)
                self.view_tree.heading('a', text='Company')
                self.view_tree.heading('b', text='Model no.')
                self.view_tree.heading('c', text='Route')
                self.view_tree.heading('d', text='Ticket Price')
                self.view_tree.heading('f', text='Total seat')
                self.view_tree.heading('g', text='Description')
                # self.for_treeview()
        except Exception as e:
            print(e)

    def select_plane(self, event):
        try:
            sel_row = self.view_tree.selection()[0]
            sel_item = self.view_tree.item(sel_row)
            self.index = self.view_tree.item(sel_row, 'text')
            selected_data = self.view_tree.item(sel_row, 'values')
            self.entry_ac.delete(0, 'end')
            self.entry_ac.insert(0, selected_data[0])
            self.entry_p.delete(0, 'end')
            self.entry_p.insert(0, selected_data[1])
            self.combox.delete(0, 'end')
            self.combox.insert(0, selected_data[2])
            self.entry_tc.delete(0, 'end')
            self.entry_tc.insert(0, selected_data[3])
            self.entry_st.delete(0, 'end')
            self.entry_st.insert(0, selected_data[4])
            self.entry_des.delete(0, 'end')
            self.entry_des.insert(0, selected_data[5])

            self.buttt = Button(self.wn1, text='Generate Ticket', command=self.gene_tic)
            self.buttt.place(x=550, y=330)
        except Exception as e:
            print(e)

    def search_button(self):
        try:
            self.database = DataBase()
            uinput = self.entry.get()
            keyword = self.entry2.get()

            if uinput == 'Route':
                qry = "SELECT * FROM plane_reg WHERE route LIKE '" + keyword + "%'"
                win = self.database.get_data_p(qry, keyword)
                print(win)

                self.view_tree.delete(*self.view_tree.get_children())
                for i in win:
                    self.view_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
                    self.view_tree.bind("<Double-1>", self.select_plane)

            elif uinput == 'Company':
                qry = "SELECT * FROM plane_reg WHERE company LIKE '" + keyword + "%'"
                win = self.database.get_data_p(qry, keyword)
                print(win)

                self.view_tree.delete(*self.view_tree.get_children())
                for i in win:
                    self.view_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
                    self.view_tree.bind("<Double-1>", self.select_plane)

            elif uinput == 'Price':
                qry = "SELECT * FROM plane_reg WHERE price LIKE '" + keyword + "%'"
                win = self.database.get_data_p(qry, keyword)
                print(win)

                self.view_tree.delete(*self.view_tree.get_children())
                for i in win:
                    self.view_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
                    self.view_tree.bind("<Double-1>", self.select_plane)

        except Exception as e:
            print(e)

    def gene_tic(self):
        try:
            self.wn7 = Toplevel()
            self.wn7.title("Ticket")
            self.wn7.geometry("400x380")
            self.wn7.configure(bg="light pink")

            self.lbl = Label(self.wn7, text="Roy Airline Services", fg="dark blue",bg='pink',
                             font=("arial", 15, "bold"))
            self.lbl.place(x=60, y=30)

            self.lbl = Label(self.wn7, text="Flight-Ticket", fg="dark blue",bg='pink',
                             font=("arial", 10, "bold"))
            self.lbl.place(x=100, y=70)

            self.lbl = Label(self.wn7, text="Company: ", fg="dark blue",
                             font=("arial", 10, "bold"))
            self.lbl.place(x=40, y=140)
            self.entry_ac = Entry(self.wn7,textvariable='a')
            self.entry_ac.place(x=120, y=140)


            self.b = Label(self.wn7, text=" Plane Route: ", fg="dark blue", font=("arial", 10, "bold"))
            self.b.place(x=15, y=170)
            self.combox = Entry(self.wn7, width=30,textvariable='b')
            self.combox.place(x=120, y=170)

            self.tc = Label(self.wn7, text="Ticket price ", fg="dark blue", font=("arial", 10, "bold"))
            self.tc.place(x=30, y=200)
            self.entry_tc = Entry(self.wn7,textvariable='c')
            self.entry_tc.place(x=120, y=200)

            self.pas_name = Label(self.wn7, text="Passanger name: ", fg="dark blue", font=("arial", 10, "bold"))
            self.pas_name.place(x=15, y=240)
            self.entry_pn =Entry(self.wn7)
            self.entry_pn.place(x=150, y=240)

            self.pas_phone = Label(self.wn7, text="Passanger contact: ", fg="dark blue", font=("arial", 10, "bold"))
            self.pas_phone.place(x=15, y=270)
            self.entry_phn = Entry(self.wn7)
            self.entry_phn.place(x=150, y=270)

            self.citi = Label(self.wn7, text="Citizenship no.: ", fg="dark blue", font=("arial", 10, "bold"))
            self.citi.place(x=15, y=300)
            self.citi_ent = Entry(self.wn7)
            self.citi_ent.place(x=150, y=300)

            self.citi = Label(self.wn7, text="Time of flight ", fg="dark blue", font=("arial", 10, "bold"))
            self.citi.place(x=15, y=330)
            self.time_ent = Entry(self.wn7)
            self.time_ent.place(x=150, y=330)

            self.dat_lbl=Label(self.wn7, text='Date')
            self.dat_lbl.place(x=260, y=80)
            self.datent= Entry(self.wn7, width=15)
            self.datent.place(x=300,y=80)

            self.store=Button(self.wn7, text='Store', command=self.data_tk)
            self.store.place(x=300, y=330)

            today = date.today()
            self.datent.insert(0,today)


            self.wn7.mainloop()
        except Exception as e:
            print(e)

    def data_tk(self):
        try:
            company=self.entry_ac.get()
            route=self.combox.get()
            price= self.entry_tc.get()
            pas_name=self.entry_pn.get()
            pas_contact=self.entry_phn.get()
            cs_no=self.citi_ent.get()
            tof=self.time_ent.get()
            date=self.datent.get()

            if pas_name==''or pas_contact=='' or cs_no==''or tof=='' or date=='':
                messagebox.showerror('Error',"Fill up entries carefully!")

            else:
                qry= '''insert into ticket (company, route, price, pas_name, pas_contact, cs_no, flighttime, date) values(%s,%s,%s,%s,%s,%s,%s,%s)'''
                vals=(company,route,price,pas_name,pas_contact,cs_no,tof,date)
                self.database.iud(qry,vals)
                messagebox.showinfo('Done',"Store success!")
        except Exception as e:
            print(e)




