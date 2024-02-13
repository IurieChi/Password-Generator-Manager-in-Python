#password generator

# to be able to encript and decript file need pip install cryptography and import Fernet
# from cryptography.fernet import Fernet

import tkinter as tk
from cryptography.fernet import Fernet

import logic as l



class MainWindow:
    #use constructor
    def __init__(self) -> None:
        self.main = tk.Tk()
        self.main.geometry('300x350') #window size 
        self.main.resizable(width=False, height=False)
        self.main.title("Password Generator")
        self.widgets()
        self.main.mainloop()
        # self.encryptPass()
        

    def widgets(self):
        self.frame = tk.Frame(self.main) #create a frame 

        self.val, self.special, self.num = tk.IntVar(),tk.IntVar(),tk.IntVar() #wariables

         #create frame with text on top
        self.oprionsFrame = tk.LabelFrame(self.frame, text='Options') 
        self.upperCase = tk.Checkbutton(self.oprionsFrame, text='Upper case leter', onvalue=1, offvalue=0, variable=self.val)
        self.specialChar = tk.Checkbutton(self.oprionsFrame, text='Special character',onvalue=1, offvalue=0, variable=self.special)
        self.number = tk.Checkbutton(self.oprionsFrame, text='Number',onvalue=1, offvalue=0, variable=self.num)

        # Length Options
        self.lengthFrame = tk.LabelFrame(self.frame, text='Password Lenght')
        self.lenght = tk.IntVar()
        self.lenght.set('8') #set default value
        # Radio Buttons
        self.radioButton1 = tk.Radiobutton(self.lengthFrame, text='8', value=8, variable=self.lenght)
        self.radioButton2 = tk.Radiobutton(self.lengthFrame, text='10', value=10, variable=self.lenght)
        self.radioButton3 = tk.Radiobutton(self.lengthFrame, text='12', value=12, variable=self.lenght)
        # Buttons && Textbox
        self.genPas = tk.Button(self.main, text='Generate Password', width=25 ,foreground='green'), #command=self.l.generatePassword)
        self.vievHis = tk.Button(self.main, width= 25, text='View History', foreground='red')#, command=self.l.getHistory)
        self.copyPass =tk.Button(self.main,width= 25, text='Copy password')#,command=self.l.copyPassword)
        self.textBox = tk.Text(self.main, width=25, height= 8, relief='solid')
        # Packing && Grid of Widgets
        self.widgetsInFrame =   [self.upperCase, self.specialChar, self.number]
        for item in self.widgetsInFrame:
            item.pack(pady =5 ,anchor ='w')
        self.radioButtons = [self.radioButton1,self.radioButton2,self.radioButton3]
        for item in self.radioButtons:
            item.pack(pady=5, anchor='w')
        self.oprionsFrame.grid(row=0, column=0) # Options and Length beside each other
        self.lengthFrame.grid(row=0, column=1) 
        self.mainWidgets = [ self.frame, self.genPas,self.copyPass,self.vievHis, self.textBox]
        for widget in self.mainWidgets: 
            widget.pack(pady=5)

 
    
if __name__ == "__main__":
    MainWindow()    