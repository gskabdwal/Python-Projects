import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"

# ---------------------------- TIMER RESET ------------------------------- #
reps = 0
time = None


def reset_timer():
    window.after_cancel(time)
    heading.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        heading.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)

    elif reps % 2 == 0:
        heading.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        heading.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(total):

    min = math.floor(total / 60)
    sec = total % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if total > 0:
        global time
        time = window.after(1000, countdown, total-1)
    else:
        timer()
        if reps % 2 == 0:
            check_mark.config(text=f"{TICK}"*int(reps/2))

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro")
window.config(padx=30, pady=10, bg=YELLOW)

canvas = Canvas(height=240, width=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=pic)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 34, "bold"), fill="white")
canvas.grid(row=1, column=1)


heading = Label(text="Timer", font=(FONT_NAME, 50, "bold"),
                fg=GREEN, bg=YELLOW, pady=20)
heading.grid(row=0, column=1)

check_mark = Label(fg=GREEN, bg=YELLOW, pady=20)
check_mark.grid(row=3, column=1)

start = Button(text="Start", highlightthickness=0, command=timer)
start.grid(row=2, column=0)

stop = Button(text="Reset", highlightthickness=0, command=reset_timer)
stop.grid(row=2, column=2)


window.mainloop()
