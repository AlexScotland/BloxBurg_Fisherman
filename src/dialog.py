from tkinter import messagebox

class Message():
    def __init__(self):
        self.type_func_mapper ={
            "Information":messagebox.showinfo,
            "Error":messagebox.showerror,
            "Warning":messagebox.showwarning
        }
    def create_dialog_message(self,type,message):
        return self.type_func_mapper[type](type,message)