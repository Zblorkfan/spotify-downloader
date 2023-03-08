


from tkinter import *
import os
from tkinter import ttk
from threading import Thread
from multiprocessing import Process
import subprocess

#Create an instance of Tkinter frame
def download():
   global entry 
   url = entry.get()

   label = Label(win, text='Téléchargement en cours...')
   label.pack(ipadx=10, ipady=10)
   win.update()
   subprocess.call("py -m spotdl download [" + url + "]",shell=True)

   label = Label(win, text='Téléchargement terminé !')
   label.pack(ipadx=10, ipady=10)
   win.update()
win= Tk()
win.title("Spotify Downloader")
#Set the geometry of Tkinter frame
win.geometry("350x190")


#Initialize a Label to display the User Input
label = Label(win, text='Entrez un lien spotify')
label.pack(ipadx=10, ipady=10)
#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()


#Create a Button to validate Entry Widget
ttk.Button(win, text= "Télécharger",width= 20, command=download).pack(pady=20)


win.mainloop()
