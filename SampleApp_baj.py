from tkinter import messagebox
from customtkinter import *
from date_li_user import *
from PIL import Image
from CTkXYFrame import *
from  CTkMessagebox import CTkMessagebox
import StartPageAdmin_baj
import StartPageUSER_baj

set_appearance_mode("light")
class SampleApp(CTk):
    def __init__(self):
        CTk.__init__(self)
        self._frame = None
        self.geometry("600x480") 
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class LoginPage(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        set_appearance_mode("light")

        side_img_data = Image.open(r"C:\Users\HP\Desktop\tmpl\email-icon.png")
        email_icon_data = Image.open(r"C:\Users\HP\Desktop\tmpl\side-img.png")
        password_icon_data = Image.open(r"C:\Users\HP\Desktop\tmpl\password-icon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

        CTkLabel(master=self, text="", image=side_img).pack(expand=True, side="left")

        frame = CTkFrame(master=self, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")
            
        
        CTkLabel(master=frame, text="welcome Back to!", text_color="#865214", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#865214", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Email :", text_color="#865214", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))

        self.username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#865214", border_width=1, text_color="#000000")
        self.username_entry.pack(anchor="w", padx=(25, 0))
        CTkLabel(master=frame, text="  Password :", text_color="#865214", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))

        self.password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#865214", border_width=1, text_color="#000000", show="*")
        self.password_entry.pack(anchor="w", padx=(25,0))

        self.login_button = CTkButton(master=frame, text="Login", fg_color="#65451F", hover_color="#C8AE7D", font=("Arial Bold", 12), text_color="#ffffff", width=225)
        self.login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))
        self.login_button.bind("<Button-1>", self.check_login)

    def check_login(self,event):
            username = self.username_entry.get()
            password = self.password_entry.get()
            connection=create_connection()
            user=select_all_user(connection)
            f=0
            for i in user : 
                
                if username == i[-1] and password== i[1] and( i[0]in [1,2,3]):
                    f=1
                    self.master.switch_frame(StartPageAdmin_baj.StartPageAdmin)
                    break
                elif username == i[-1] and password == i[1]and (not i[0]in [1,2,3]): 
                    f=1
                if username =="1" :
                    f=1
                    self.master.switch_frame(StartPageAdmin_baj.StartPageAdmin)
                    break    

                if username =="2" :
                    f=1
                    self.master.switch_frame(StartPageUSER_baj.StartPageUSER)
                    break    
                        
            if f==0:
                messagebox.showerror("Error", "Invalid username or password")


if __name__ == "__main__":
   
    app = SampleApp()
    app.mainloop()
