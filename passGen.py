#password generator
import string, random
import tkinter as tk

class MainWindow:
    #use constructor
    def __init__(self) -> None:
        self.main = tk.Tk()
        self.main.geometry('300x350') #window size 
        self.main.resizable(width=False, height=False)
        self.main.title("Password Generator")
        self.widgets()
        self.main.mainloop()

    def widgets(self):
        self.frame = tk.Frame(self.main) #create a frame 

        self.val, self.special, self.num = tk.IntVar(),tk.IntVar(),tk.IntVar() #wariables
        self.oprionsFrame = tk.LabelFrame(self.frame, text='Options') #create frame with test on top 
        self.upperCase = tk.Checkbutton(self.oprionsFrame, text='Upper case leter', onvalue=1, offvalue=0, variable=self.val)
        self.specialChar = tk.Checkbutton(self.oprionsFrame, text='Special character',onvalue=1, offvalue=0, variable=self.special)
        self.number = tk.Checkbutton(self.oprionsFrame, text='Numer',onvalue=1, offvalue=0, variable=self.num)

        # Length Options
        self.lenght = tk.IntVar()
        self.lenght.set('8') #set default value
        self.lengthFrame = tk.LabelFrame(self.frame, text='Password Lenght')
        # Radio Buttons
        self.radioButton1 = tk.Radiobutton(self.lengthFrame, text='8', value=8, variable=self.lenght)
        self.radioButton2 = tk.Radiobutton(self.lengthFrame, text='10', value=10, variable=self.lenght)
        self.radioButton3 = tk.Radiobutton(self.lengthFrame, text='12', value=12, variable=self.lenght)
        # Buttons && Textbox
        self.genPas = tk.Button(self.main, text='Generate Password', width=25, command=self.generatePassword)
        self.vievHis = tk.Button(self.main, width= 25, text='View History', command=self.getHistory)
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
        self.mainWidgets = [ self.frame, self.genPas, self.vievHis, self.textBox ]
        for widget in self.mainWidgets: 
            widget.pack(pady=5)

    def generatePassword(self):
        if self.val.get() == 1:
            randomUpper = random.choices(string.ascii_uppercase, k=5)
        else:randomUpper = []
        if self.special.get() ==1:
            randomSpecial = random.choices("-_@!?.", k=2)
        else:randomSpecial=[]
        if self.num.get()==1:
            randomNum = random.choices(string.digits, k=5)
        else:randomNum =[]
        randomGen = random.sample(randomUpper + randomSpecial + randomNum + random.choices(string.ascii_lowercase, k=12), k= int(self.lenght.get()))
        #populate textbox
        self.textBox.config(state='normal')
        self.textBox.delete(1.0,'end')
        self.textBox.insert(1.0, f'{"".join(randomGen)}\n')
        self.textBox.config(state='disabled')
        with open('password.txt','a') as file: file.write(f"{''.join(randomGen)}\n")


    def getHistory(self):
        self.textBox.config(state='normal')
        self.textBox.delete(1.0, 'end')
        self.textBox.insert(1.0, open('password.txt','r').read())
        self.textBox.config(state='disabled')

if __name__ == "__main__":
    MainWindow()    