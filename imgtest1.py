__author__ = 'Administrator'
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        # self.helloLabel=Label(self,text='Hello,World')

        # self.helloLabel.pack()
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.quitButton=Button(self,text='quit',command=self.hello)
        self.quitButton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'%name)
app=Application()
app.master.title('Hello World')
app.mainloop()
