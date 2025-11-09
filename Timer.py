import tkinter as tk
import time

window = tk.Tk()
window.title("Timer App")
window.geometry("800x800")
window.configure(bg = "#dad7cd")

heading = tk.Label(window, text = "Timer App", font = ("Verdana", 30), fg = "#344e41", bg = "#a3b18a", width = 50, height = 2)
heading.pack()

isPaused = False
tempTime = 0

def timer():

    h.config(state = "disabled")
    m.config(state = "disabled")
    s.config(state = "disabled")

    try:
        tempTime = int(h.get()) * 3600 + int(m.get()) * 60 + int(s.get())
        print(tempTime)
    
    except:
        print('Please input the correct values (integer values)')

    while tempTime > -1:
        if isPaused:
            break

        min, sec = divmod(tempTime, 60)
        hour = 00

        if min > 60:
            hour, min = divmod(min, 60)

        print(hours, minutes, seconds)
        hours.set(f"{hour : 2d}")
        minutes.set(f"{min : 2d}")
        seconds.set(f"{sec : 2d}")

        window.update()

        time.sleep(1)
        tempTime = tempTime -1

def stopTimer():
    global isPaused

    isPaused = True


def resumeTimer():
    global isPaused

    if isPaused:
        isPaused = False
        timer()


hours = tk.StringVar(value = "00")
minutes = tk.StringVar(value = "00")
seconds = tk.StringVar(value = "00")

h = tk.Entry(window, font = ("Verdana", 40), bg = "#dad7cd", textvariable = hours, justify = 'center', width = 5)
h.place(x = 125, y = 150)

m = tk.Entry(window, font = ("Verdana", 40), bg = "#dad7cd", textvariable = minutes, justify = 'center', width = 5)
m.place(x = 325, y = 150)

s = tk.Entry(window, font = ("Verdana", 40), bg = "#dad7cd", textvariable = seconds, justify = 'center', width = 5)
s.place(x = 525, y = 150)

startBtn = tk.Button(window, text = "Start", font = ("Verdana", 20), bg = "#dad7cd", command = timer, width = 10)
startBtn.place(x = 325, y = 300)

stopBtn = tk.Button(window, text = 'Stop', font = ('Verdana', 20), bg = "#dad7cd", command = stopTimer, width = 10)
stopBtn.place(x = 325, y = 400)

resumeBtn = tk.Button(window, text = 'Resume', font = ('Verdana', 20), bg = "#dad7cd", command = resumeTimer, width = 10)
resumeBtn.place(x = 325, y = 500)


window.mainloop()