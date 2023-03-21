from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import Api
class NLPApp():


    def __init__(self):
        # create object of Database class
        self.dbo = Database()
        self.api = Api()

        # login gui
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        
        self.root.geometry('300x600')
        self.root.config(bg = 'grey')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='grey', fg='white')
        heading.pack(pady=(30,30))
        heading.config(font=('verdana',24,'bold'))

        lable1 = Label(self.root, text= 'Enter email')
        lable1.pack(pady=(10,10))
        self.email_input =Entry(self.root, width=40)
        self.email_input.pack(pady=(5,10),ipady=5)

        lable2 = Label(self.root, text='Enter password')
        lable2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        login_btn =Button(self.root, text='login', width=20, height=2, command= self.perform_login)
        login_btn.pack(pady=(10,10))

        lable3 = Label(self.root, text='Not a member')
        lable3.pack(pady=(10, 10))

        register_btn = Button(self.root, text='Register', width=20, height=2, command= self.register_gui)
        register_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='grey', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        lable0 = Label(self.root, text='Enter name')
        lable0.pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(5, 10), ipady=5)

        lable1 = Label(self.root, text='Enter email')
        lable1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=5)

        lable2 = Label(self.root, text='Enter password')
        lable2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        lable3 = Label(self.root, text='Confirm password')
        lable3.pack(pady=(10, 10))
        self.password2_input = Entry(self.root, width=40, show='*')
        self.password2_input.pack(pady=(5, 10), ipady=5)

        register_btn = Button(self.root, text='Register', width=20, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        lable4 = Label(self.root, text='Already a member')
        lable4.pack(pady=(10, 10))

        login_btn = Button(self.root, text='Login', width=20, height=2, command=self.login_gui)
        login_btn.pack(pady=(10, 10))

    def clear(self):
        #clear existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        #fetch data from gui
        name =self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        password2 = self.password2_input.get()

        response = self.dbo.pass_check(password,password2)
        if response:
            response2= self.dbo.add_data(name,email,password)
            if response2:
                messagebox.showinfo('Success','Registration Successful')
            else:
                messagebox.showerror('Error', 'Email Exists')

        else:
            messagebox.showerror('Error', 'Enter correct password')


    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Wrong email or password\nTry again')

    def home_gui(self):
        #create home page
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='grey', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', width=20, height=2, command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='grey', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='grey', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.config(font=('verdana', 20,))

        lable1 = Label(self.root, text='Enter Text')
        lable1.pack(pady=(10, 10))
        self.sentiment_input = Entry(self.root, width=40)
        self.sentiment_input.pack(pady=(5, 10), ipady=5)

        analyse_btn = Button(self.root, text='Analyse', width=20, height=2, command=self.do_sentiment_analysis)
        analyse_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg= 'grey', fg= 'white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.config(font=('verdana', 14,))

        home_btn = Button(self.root, text='Home', width=20, height=2, command=self.home_gui)
        home_btn.pack(pady=(10, 10))


    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='grey', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='grey', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.config(font=('verdana', 20,))

        lable1 = Label(self.root, text='Enter Text')
        lable1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=40)
        self.ner_input.pack(pady=(5, 10), ipady=5)


        find_btn = Button(self.root, text='Find', width=20, height=2, command=self.do_ner)
        find_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='grey', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.config(font=('verdana', 14,))

        home_btn = Button(self.root, text='Home', width=20, height=2, command=self.home_gui)
        home_btn.pack(pady=(10, 10))


    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='grey', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Prediction', bg='grey', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.config(font=('verdana', 20,))

        lable1 = Label(self.root, text='Enter Text')
        lable1.pack(pady=(10, 10))
        self.emotion_input = Entry(self.root, width=40)
        self.emotion_input.pack(pady=(5, 10), ipady=5)

        find_btn = Button(self.root, text='Find', width=20, height=2, command=self.do_emotion_prediction)
        find_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='grey', fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.config(font=('verdana', 14,))

        home_btn = Button(self.root, text='Home', width=20, height=2, command=self.home_gui)
        home_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.api.sentiment_analysis(text)

        self.sentiment_result['text'] = result

    def do_ner(self):
        text = self.ner_input.get()
        result = self.api.ner(text)

        self.ner_result['text'] =  result

    def do_emotion_prediction(self):
        text = self.emotion_input.get()
        result = self.api.emotion_prediction(text)

        self.emotion_result['text'] = result



nlp = NLPApp()
