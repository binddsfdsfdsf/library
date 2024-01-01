from customtkinter import *
from CTkTable import CTkTable
from date_li_user import *
from CTkXYFrame import *
from  CTkMessagebox import CTkMessagebox
import StartPageAdmin_Borrow_baj
import StartPageAdmin_baj
class StartPageAdmin_use(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        master.pack_propagate(0)
        master.geometry("856x645") 
        master.resizable(0,0)
        set_appearance_mode("light")

        self.sidebar_frame = CTkFrame(master=self, fg_color="#765827", width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        CTkButton(master=self.sidebar_frame, text="Books", fg_color="transparent", font=("Arial Bold", 14), hover_color="#BF9270", anchor="w",command=self.to_Book).pack(anchor="center", padx=5, pady=(16, 0))
        CTkButton(master=self.sidebar_frame, text="Users", fg_color="#fff", font=("Arial Bold", 14), text_color="#765827",hover_color="#C8AE7D", anchor="w",command=self.to_now).pack(anchor="center", padx=5, pady=(16, 0))
        CTkButton(master=self.sidebar_frame, text="Borrow", fg_color="transparent", font=("Arial Bold", 14), hover_color="#BF9270", anchor="w",command=self.to_Borrow).pack(anchor="center", padx=5, pady=(16, 0))

        self.sidebar_frame.pack(anchor="w", side="left", fill="y", expand=True)

        self.main_view = CTkFrame(master=self, fg_color="#fff", corner_radius=0, width=680, height=650)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        CTkLabel(master=self.title_frame, text="Users", font=("Arial Black", 25), text_color="#765827").pack(anchor="nw", side="left")
        CTkButton(master=self.title_frame, text="New User", font=("Arial Black", 15), text_color="#fff", fg_color="#765827", hover_color="#BF9270", command=self.open_toplevel).pack(anchor="ne", side="right")
        CTkButton(master=self.title_frame, text="Delete User", font=("Arial Black", 15), text_color="#fff", fg_color="#765827", hover_color="#BF9270",command=self.open_toplevelDel).pack(anchor="ne", side="right",padx=12)
        CTkButton(master=self.title_frame, text="Updat User", font=("Arial Black", 15), text_color="#fff", fg_color="#765827", hover_color="#BF9270",command=self.open_toplevelUp).pack(anchor="ne", side="right",padx=8)
        self.search_container = CTkFrame(master=self.main_view, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(45, 0), padx=27)
        self.entry=CTkEntry(master=self.search_container, width=305 ,border_color="#765827", border_width=2, placeholder_text="Search Book")
        self.entry.pack(side="left", padx=(13, 0), pady=15)
        self.text = self.entry.get()
        print(self.text)
        CTkButton(master=self.search_container, text="Search", font=("Arial Black", 15), text_color="#fff", fg_color="#765827", hover_color="#BF9270",command=self.to_search).pack(anchor="ne",padx=13, pady=15)
        connection=create_connection()
        self.table_data=select_all_user(connection)
        print(self.table_data)
        self.table_frame = CTkXYFrame(master=self.main_view)
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#765827", hover_color="#B4B4B4")

        self.table.edit_row(0, text_color="#fff", hover_color="#765827")
        self.table.pack(expand=True)
        self.main_view.pack(side="left", fill="both", expand=True)
        self.toplevel_window = None
    def to_Borrow(self):
        self.master.switch_frame(StartPageAdmin_Borrow_baj.StartPageAdmin_Borrow)
    def to_now(self):
        self.master.switch_frame(StartPageAdmin_use)
    def to_Book(self):
        self.master.switch_frame(StartPageAdmin_baj.StartPageAdmin)
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self,self.master)  
        else:
            self.toplevel_window.focus() 
    def open_toplevelUp(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowUp(self,self.master) 
        else:
            self.toplevel_window.focus()
    def open_toplevelDel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowDel(self,self.master)  
        else:
            self.toplevel_window.focus() 
    def to_search(self):
        self.inx=len(self.table_data)
        connection=create_connection()
        f=0
        self.tab=self.entry.get()
        self.args=search_user(connection,self.tab)
        self.args2=select_all_user(connection)
        print(self.args)
        for i in self.args2:
            if self.args[1]==i:
                self.i=self.args2.index(i)
        print(self.inx)
        for num in  range(1,self.inx):
            if num==self.i:

                continue
            self.table.delete_row(num)

class ToplevelWindow(CTkToplevel):

    def __init__(self, master,*args, **kwargs):
        self.master=master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("GotchaTube!")
        self.geometry("550x160")
        self.resizable(width = False ,height = False)
        self.configure(bg='#fff')
        set_appearance_mode("light")

        self.title = CTkEntry(
            master=self,
            border_color="#765827",
            placeholder_text='Name',
            width= 200,
            height=35,
        )
        self.kentry1 = CTkEntry(
            master=self,
            border_color="#765827",
            placeholder_text='First name',
            width= 200,
            height=35,
        )
        self.kentry2 = CTkEntry(
            master=self,
        border_color="#765827",
            placeholder_text='Date of birth',
            width= 200,
            height=35,
        )
        self.kentry3 = CTkEntry(
            master=self,
        border_color="#765827",
            placeholder_text='Email',
            width= 200,
            height=35,
        )
        self.kentry4 = CTkEntry(
            master=self,
        border_color="#765827",
            placeholder_text='ID',
            width= 200,
            height=35,
        )
        # exitPath = CTkEntry(
        #     master=self,
        #     border_color="#765827",
        #     placeholder_text='File exit path',
        #     width= 200,
        #     height=35,
        # )

        button = CTkButton(
            master=self,
            text="New",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,
            hover_color= "#B0926A",
            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,
            border_color= "#fff", 
            bg_color="#FAEED1",
            fg_color= "#765827",
     command=self.user_NEW

        )
        self.title.place(x= 18, y= 20)
        self.kentry1.place(x= 236, y= 20)
        self.kentry2.place(x= 18, y=65 )
        self.kentry3.place(x= 236, y=65 )
        self.kentry4.place(x= 18, y=110 )

        button.place(x= 236, y= 110)

    def user_NEW(self):
            
        self.texit = self.title.get()
        self.texit1 = self.kentry1.get()
        self.texit2 = self.kentry2.get()
        self.texit3 = self.kentry3.get()
        self.texit4 = int(self.kentry4.get())
        connection=create_connection()
        insert_user(connection,self.texit4,self.texit,self.texit1,self.texit2,self.texit3)
        self.destroy()
        self.master.switch_frame(StartPageAdmin_use)
    

class ToplevelWindowDel(CTkToplevel):

    def __init__(self, master,*args, **kwargs):
        self.master=master

        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("GotchaTube!")
        self.geometry("550x160")
        self.resizable(width = False ,height = False)
        self.configure(bg='#fff')

        set_appearance_mode("light")

        self.title = CTkEntry(
            master=self,
            border_color="#765827",
            placeholder_text='User ID',
            width= 200,
            height=35,
        )


        Button = CTkButton(
            master=self,
            text="Delet",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,
            hover_color= "#B0926A",
            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,
            border_color= "#fff", 
            bg_color="#FAEED1",
            fg_color= "#765827",
            command=self.user_del
        )

        self.title.place(x= 18, y= 20)

        Button.place(x= 236, y= 20)
    def user_del(self):
        self.texit = self.title.get()
        connection=create_connection()
        delete_user(connection,self.texit)
        self.destroy()
        self.master.switch_frame(StartPageAdmin_use)
class ToplevelWindowUp(CTkToplevel):

    def __init__(self, master,*args, **kwargs):
        self.master=master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("GotchaTube!")
        self.geometry("550x160")
        self.resizable(width = False ,height = False)
        self.configure(bg='#fff')
        set_appearance_mode("light")

        self.title = CTkEntry(
            master=self,
            border_color="#765827",
            placeholder_text='Name',
            width= 200,
            height=35,
        )
        self.kentry1 = CTkEntry(
            master=self,
            border_color="#765827",
            placeholder_text='First name',
            width= 200,
            height=35,
        )
        self.kentry2 = CTkEntry(
            master=self,
        border_color="#765827",
            placeholder_text='Date of birth',
            width= 200,
            height=35,
        )
        self.kentry3 = CTkEntry(
            master=self,
        border_color="#765827",
            placeholder_text='Email',
            width= 200,
            height=35,
        )
        self.kentry4 = CTkEntry(
            master=self,
        border_color="#765827",
            placeholder_text='ID',
            width= 200,
            height=35,
        )
        # exitPath = CTkEntry(
        #     master=self,
        #     border_color="#765827",
        #     placeholder_text='File exit path',
        #     width= 200,
        #     height=35,
        # )

        button = CTkButton(
            master=self,
            text="New",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,
            hover_color= "#B0926A",
            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,
            border_color= "#fff", 
            bg_color="#FAEED1",
            fg_color= "#765827",
     command=self.user_NEW

        )
        self.title.place(x= 18, y= 20)
        self.kentry1.place(x= 236, y= 20)
        self.kentry2.place(x= 18, y=65 )
        self.kentry3.place(x= 236, y=65 )
        self.kentry4.place(x= 18, y=110 )

        button.place(x= 236, y= 110)

    def user_NEW(self):
            
        self.texit = self.title.get()
        self.texit1 = self.kentry1.get()
        self.texit2 = self.kentry2.get()
        self.texit3 = self.kentry3.get()
        self.texit4 = int(self.kentry4.get())
        connection=create_connection()
        update_user(connection,self.texit4,self.texit,self.texit1,self.texit2,self.texit3)
        self.destroy()
        self.master.switch_frame(StartPageAdmin_use)
    
