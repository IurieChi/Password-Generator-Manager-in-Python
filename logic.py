# import passGen 
import string
import random
from tkinter import messagebox
import pyperclip as clipboard
from cryptography.fernet import Fernet

key = b'4b6LWAOo3Y1mgjTIjOMSAdz2LPaKFNvCfdKv1Vzg-Lc='
token = Fernet(key)

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