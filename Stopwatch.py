import tkinter as tk
import time

window = tk.Tk()
window.title('Stopwatch')
window.geometry('800x800')

heading = tk.Label(window, text='Stopwatch App', font=('Verdana', 30), fg='#03045e', bg='#90e0ef', width=200, height=2)
heading.pack()

hours = tk.StringVar(value="00")
minutes = tk.StringVar(value="00")
seconds = tk.StringVar(value="00")

isPaused = False
isRunning = False
elapsedTime = 0

def updateDisplay():
    global elapsedTime
    mins, secs = divmod(elapsedTime, 60)
    hrs = 0
    if mins >= 60:
        hrs, mins = divmod(mins, 60)

    hours.set(f"{hrs:02d}")
    minutes.set(f"{mins:02d}")
    seconds.set(f"{secs:02d}")

def runStopwatch():
    global elapsedTime, isPaused, isRunning
    isRunning = True
    isPaused = False

    while isRunning and not isPaused:
        updateDisplay()
        window.update()
        time.sleep(1)
        elapsedTime += 1

def startStopwatch():
    global isRunning
    if not isRunning:
        runStopwatch()

def stopStopwatch():
    global isPaused
    isPaused = True

def resumeStopwatch():
    global isPaused
    if isPaused:
        isPaused = False
        runStopwatch()


h = tk.Entry(window, font=("Verdana", 40), bg="#dad7cd", justify='center', width=5, textvariable=hours, state="disabled")
h.place(x=125, y=150)

m = tk.Entry(window, font=("Verdana", 40), bg="#dad7cd", justify='center', width=5, textvariable=minutes, state="disabled")
m.place(x=325, y=150)

s = tk.Entry(window, font=("Verdana", 40), bg="#dad7cd", justify='center', width=5, textvariable=seconds, state="disabled")
s.place(x=525, y=150)

startBtn = tk.Button(window, text="Start", font=("Verdana", 20), bg="#dad7cd", width=10, command=startStopwatch)
startBtn.place(x=325, y=300)

stopBtn = tk.Button(window, text='Stop', font=('Verdana', 20), bg="#dad7cd", width=10, command=stopStopwatch)
stopBtn.place(x=325, y=400)

resumeBtn = tk.Button(window, text='Resume', font=('Verdana', 20), bg="#dad7cd", width=10, command=resumeStopwatch)
resumeBtn.place(x=325, y=500)

window.mainloop()
