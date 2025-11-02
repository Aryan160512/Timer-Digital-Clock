import tkinter as tk
from time import strftime

window = tk.Tk()
window.title('Digital Clock')
window.geometry('800x800')
window.configure(bg = '#dee2e6')

heading = tk.Label(window, text = 'Digital Clock', font = ('Verdana', 30), fg = '#adb5bd', bg = '#212529', width = 200, height = 2)
heading.pack()

def digTime():
    date = strftime('Time: %I : %M : %S : %p  \n \n Date: %d / %m / %y  \n \n Time Zone: %z \n \n Full Date: %A %d %B %Y')
    dateLabel.config(text = date)
    dateLabel.after(1000, digTime)
    

dateLabel = tk.Label(window, text = 'Digital Clock', font = ('Verdana', 20), bg = '#dee2e6')
dateLabel.pack(pady = 20)   
button = tk.Button(window, text = 'Show Time', font = ('Verdana', 20), bg = '#dee2e6', command = digTime)
button.pack(pady = 20)

window.mainloop()
