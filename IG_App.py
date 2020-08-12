import tkinter as tk
from igbot import Ig_Bot
from threading import Thread
from time import sleep

def ok(*args):
    #Check username & password
    if text_username.get() != '' and text_password.get() != '':
        Igbot = Ig_Bot(text_username.get(), text_password.get())
        #Create window
        window = tk.Tk()
        window.geometry('350x500')
        window.title(text_username.get()+' IG')
        
        alert = tk.Label(
            window, text='Only One Action At Time Please!!', fg='blue')
        alert.grid(row=0, columnspan=3, padx=20, pady=5)
        #Suggestion Button
        suggested = tk.Button(
            window, text='Follow Suggested', command=Igbot.contrl_suggestions)
        suggested.grid(row=1, columnspan=3, padx=20, pady=5)
        #Suggestion Button

        #Follow page followers
        pagetxt = tk.Label(
            window, text='Enter a page to follow its followers:')
        page_warning = tk.Label(
            window, text='*Carefull the page should have open followers to see!!!', fg='red')
        pagetxt.grid(row=2, columnspan=3, padx=20, pady=5)
        page_warning.grid(row=3, columnspan=3, padx=20, pady=5)
        page = tk.Entry(window, width=35)
        page.grid(row=4, column=0, columnspan=2, padx=20, pady=5)
        page_followers = tk.Button(window,
                                   text='Page Followers', command=lambda: Igbot.contrl_get_followers(page.get()))
        page_followers.grid(row=4, column=2, pady=5)
        #Follow page followers

        #Accept Followers
        accept = tk.Button(window, text='Accept Requests!',
                           command=Igbot.contrl_accept)
        accept.grid(row=6, columnspan=3, padx=20, pady=10)
        #Acept Followers
    #Missing username or password
    else:
        username.config(text='Username *Required!', fg='red')
        password.config(text='Password *Required!', fg='red')


window = tk.Tk()
window.geometry('450x550')
window.title('IG Bot App')
label = tk.Label(window, text='Log-In', font=('50'),
                 bg='blue', width=30, height=5, fg='white')
label.grid(row=0, columnspan=3, padx=20, pady=5)
# Username Form
username = tk.Label(window, text='Username: ')
username.grid(
    row=1, columnspan=3, padx=20, pady=20)
text_username = tk.Entry(window, width=50)
text_username.grid(row=2, columnspan=3, padx=20, pady=20)
# Password Form
password = tk.Label(window, text='Password: ')
password.grid(row=3, columnspan=3, padx=20, pady=20)
text_password = tk.Entry(window, width=50)
text_password.grid(row=4, columnspan=3,  padx=20, pady=20)
text_password.bind('<Return>', ok)
# Login Button Form
login = tk.Button(window, text='Log In', width=20,
                  command=ok)
login.grid(row=5, columnspan=3, padx=20, pady=20)
# Quit Button Form
button = tk.Button(window, text='Quit', width=20, command=window.destroy)
button.grid(row=6, columnspan=3, pady=50)

window.mainloop()
