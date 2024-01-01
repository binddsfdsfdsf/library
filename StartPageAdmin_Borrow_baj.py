from customtkinter import *
from CTkTable import CTkTable
from date_li_borrow import *
from CTkXYFrame import *
import StartPageAdmin_baj 
import StartPageAdmin_use_baj
from  CTkMessagebox import CTkMessagebox
class StartPageAdmin_Borrow(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        master.pack_propagate(0)
        master.geometry("856x645") 
        master.resizable(0,0)
        set_appearance_mode("light")

        self.sidebar_frame = CTkFrame(master=self, fg_color="#765827", width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        CTkButton(master=self.sidebar_frame, text="Books", fg_color="transparent", font=("Arial Bold", 14), hover_color="#BF9270", anchor="w",command=self.to_Book).pack(anchor="center", padx=5, pady=(16, 0))
        CTkButton(master=self.sidebar_frame, text="Users", fg_color="transparent", font=("Arial Bold", 14), hover_color="#BF9270", anchor="w",command=self.to_user).pack(anchor="center", padx=5, pady=(16, 0))
        CTkButton(master=self.sidebar_frame, text="Borrow", fg_color="#fff", font=("Arial Bold", 14), text_color="#765827", anchor="w",hover_color="#C8AE7D",command=self.to_now).pack(anchor="center", padx=5, pady=(16, 0))
        self.sidebar_frame.pack(anchor="w", side="left", fill="y", expand=True)

        self.main_view = CTkFrame(master=self, fg_color="#fff", corner_radius=0, width=680, height=650)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        CTkLabel(master=self.title_frame, text="Borrow", font=("Arial Black", 25), text_color="#765827").pack(anchor="nw", side="left")

        self.search_container = CTkFrame(master=self.main_view, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(45, 0), padx=27)
        
        CTkButton(master=self.title_frame, text="Borrow Book", font=("Arial Black", 15), text_color="#fff", fg_color="#765827", hover_color="#BF9270",command=self.Borrow_Book).pack(anchor="ne", side="right",padx=12)

        self.Search_Entry=CTkEntry(master=self.search_container, width=305 ,border_color="#765827", border_width=2, placeholder_text="Search Book")
        self.Search_Entry.pack(side="left", padx=(13, 0), pady=15)

        CTkButton(master=self.search_container, text="Search", font=("Arial Black", 15), text_color="#fff", fg_color="#765827", hover_color="#BF9270",command=self.to_search).pack(anchor="ne",padx=13, pady=15)
        connection=create_connection()
        self.table_data=select_all_borrows(connection)
        self.table_frame = CTkXYFrame(master=self.main_view)
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#765827", hover_color="#B4B4B4")

        self.table.edit_row(0, text_color="#fff", hover_color="#765827")
        self.table.pack(expand=True)
        self.main_view.pack(side="left", fill="both", expand=True)
        self.toplevel_window = None
    def to_user(self):
        self.master.switch_frame(StartPageAdmin_use_baj.StartPageAdmin_use)
    def to_Book(self):
        self.master.switch_frame(StartPageAdmin_baj.StartPageAdmin)
    def to_now(self):
        self.master.switch_frame(StartPageAdmin_Borrow)
    def to_search(self):
        self.inx=len(self.table_data)
        connection=create_connection()
        f=0
        self.tab=self.Search_Entry.get()
        self.args=search_borrow(connection,self.tab)
        self.args2=select_all_borrows(connection)
        for i in self.args2:
            if self.args[1]==i:
                self.i=self.args2.index(i)
        print(self.inx)
        for num in  range(1,self.inx):
            if num==self.i:

                continue
            self.table.delete_row(num)
    # def select_and_search(self):
    #     connection=create_connection()
    #     self.text=self.Search_Entry.get()
    #     if self.text=="":
    #         return select_all_books(connection)
    #     else:
    #         return search_book(connection,self.text)
        
    def Borrow_Book(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindowBor_boo(self)  
            else:
                self.toplevel_window.focus() 
            
class ToplevelWindowBor_boo(CTkToplevel):
    def __init__(self, *args, **kwargs):
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
            text="Borrow",
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
            command=self.Borrow_Book1
        )

        self.title.place(x= 18, y= 20)

        Button.place(x= 236, y= 20)
    def Borrow_Book1(self):
        self.text=self.title.get()
        print(self.text)
        connection=create_connection()
        self.Borrow=search_borrow(connection,self.text)
        print(self.text)
        if self.Borrow is None:
            CTkMessagebox(message="the book is not available",title="Error",title_color	="#000",button_hover_color="#C8AE7D",
                  icon="cancel", option_1="ok",button_color="#765827")
        else:
            CTkMessagebox(message="the book is available",title="Notice",title_color	="#000",button_hover_color="#C8AE7D",
                  icon="check", option_1="ok",button_color="#765827")
        self.destroy()
