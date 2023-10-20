#password generator
import string, random
import tkinter as tk
from tkinter import messagebox
import pyperclip as clipboard
from cryptography.fernet import Fernet

key = b'4b6LWAOo3Y1mgjTIjOMSAdz2LPaKFNvCfdKv1Vzg-Lc='
token = Fernet(key)

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
        self.genPas = tk.Button(self.main, text='Generate Password', width=25 ,foreground='green', command=self.generatePassword,)
        self.vievHis = tk.Button(self.main, width= 25, text='View History', foreground='red', command=self.getHistory)
        self.copyPass =tk.Button(self.main,width= 25, text='Copy password',command=self.copyPassword)
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

    # to be able to encript and decript file need pip install cryptography and import Fernet
        # from cryptography.fernet import Fernet
   
    def generatePassword(self):
        if self.val.get() == 1:
            randomUpper = random.choices(string.ascii_uppercase, k=5)
        else:randomUpper = []
        if self.special.get() == 1:
            randomSpecial = random.choices("-_@!?$#%^&*.", k=2)
        else:randomSpecial=[]
        if self.num.get()== 1:
            randomNum = random.choices(string.digits, k=5)
        else:randomNum =[]

        randomGen = random.sample(randomUpper + randomSpecial + randomNum + random.choices(string.ascii_lowercase, k=12), k = int(self.lenght.get()))
        #populate textbox
        genetated_password = "".join(randomGen)
        self.textBox.config(state='normal')
        self.textBox.delete(1.0,'end')
        self.textBox.insert(1.0, genetated_password)
        self.textBox.config(state='disabled')
        #encrypt generated password and save it on file
        
        encrypted = token.encrypt(genetated_password.encode())
        with open('password.txt','ab') as file: 
            file.write(encrypted + b'\n') #add password to file


    def getHistory(self):
        self.textBox.config(state='normal')
        self.textBox.delete(1.0, 'end')
        
        with open('password.txt','r')as text:
            for line in text:
                if line != '\n':
                    readEncrypted = token.decrypt(line.encode())
                    self.textBox.insert(1.0, readEncrypted)
                    self.textBox.insert(1.0,'\n')
        self.textBox.config(state='disabled')
    
    def copyPassword(self):
        #message 
        msg = 'Password copied succesfuly'
        msg_generate = 'First generate password'

        self.textBox.config(state='normal')
        if self.textBox.get(1.0,'end')=='\n':
           messagebox.showwarning('Warning',msg_generate)

        elif len(self.textBox.get(1.0,'end'))>=1 and len(self.textBox.get(1.0,'end'))<=13:
           #to copy password need to: pip install pyperclip then import pyperclip 
            clipboard.copy(self.textBox.get(1.0,'end'))
            messagebox.showinfo('message', msg)
            self.textBox.delete(1.0,'end')
        else:
            with open('password.txt','r') as text:
                for line in text:# read all file and copy just last password from for iteration 
                    pass
                    readEncrypted = token.decrypt(line.encode()) 
                clipboard.copy(readEncrypted.decode('utf-8'))   
                messagebox.showinfo('message', msg)
                self.textBox.delete(1.0,'end')
        self.textBox.config(state='disabled')



    
if __name__ == "__main__":
    MainWindow()    