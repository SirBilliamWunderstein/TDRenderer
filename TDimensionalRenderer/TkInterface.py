import DependencyObjects as dodo
import FileReader as fr
import tkinter as tk

class Window(tk.Tk):
    global disp_F
    global can
    
    def __init__(self):
        self.super().__init__()
        
        self.disp_F = tk.Frame(self,width = 1080,height = 700)
        
        self.can = tk.PhotoImage(width = 1080,height=700)
    
    def load_img(self):
        pass

objI = fr.File_create("./tesfil")
obj = dodo.objection(objI[1],objI[0])
print(obj.Frel)
print(obj.P)