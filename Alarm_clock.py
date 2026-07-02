import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
import winsound

alarm_running = False
alarm_triggered = False


def check_alarm():
    global alarm_running, alarm_triggered

    while alarm_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time.get():
            alarm_triggered = True
            status_label.config(text=" Alarm Ringing!", fg="red")

            while alarm_triggered:
                winsound.Beep(1000, 500)

            break

        time.sleep(1)


def set_alarm():
    global alarm_running

    alarm = alarm_time.get()

    try:
        datetime.datetime.strptime(alarm, "%H:%M:%S")
    except ValueError:
        messagebox.showerror("Invalid Time", "Enter time in HH:MM:SS format")
        return

    if not alarm_running:
        alarm_running = True
        status_label.config(text=f"Alarm Set for {alarm}", fg="green")

        thread = threading.Thread(target=check_alarm)
        thread.daemon = True
        thread.start()


def stop_alarm():
    global alarm_triggered, alarm_running
    alarm_triggered = False
    alarm_running = False
    status_label.config(text="Alarm Stopped", fg="blue")


def update_clock():
    current = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current)
    root.after(1000, update_clock)


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="Alarm Clock", font=("Arial", 20, "bold"))
title.pack(pady=10)

clock_label = tk.Label(root, font=("Arial", 24), fg="blue")
clock_label.pack()

tk.Label(root, text="Enter Alarm Time (HH:MM:SS)",
         font=("Arial", 12)).pack(pady=10)

alarm_time = tk.StringVar()

entry = tk.Entry(root,
                 textvariable=alarm_time,
                 font=("Arial", 16),
                 justify="center")
entry.pack()

set_btn = tk.Button(root,
                    text="Set Alarm",
                    font=("Arial", 12),
                    bg="green",
                    fg="white",
                    command=set_alarm)
set_btn.pack(pady=10)

stop_btn = tk.Button(root,
                     text="Stop Alarm",
                     font=("Arial", 12),
                     bg="red",
                     fg="white",
                     command=stop_alarm)
stop_btn.pack()

status_label = tk.Label(root,
                        text="No Alarm Set",
                        font=("Arial", 12))
status_label.pack(pady=15)

update_clock()

root.mainloop()