from tkinter import *
import keyboard


Font = ('Arial', 12, 'normal')
session_time = 20
stop_timer = None
session_stop_timer = None
is_on = True
stop_sec = 5


def start():
    global session_time, stop_timer, stop_sec
    entry.delete("1.0", END)
    entry.config(state=NORMAL)
    entry.focus()

    if is_on:
        time_text.config(text=session_time)
        windows.update()
        if keyboard.read_key():
            stop_sec_count_down(stop_sec)
            count_down(session_time)


def count_down(session_time):
    global session_timer
    if session_time > 0:
        session_timer = windows.after(1000, count_down, session_time - 1)
        session_time -= 1
        time_text.config(text=session_time)
        windows.update()

        if session_time == 0:
            entry.config(state=DISABLED)
            windows.update()


def stop_sec_count_down(stop_sec):
    global stop_timer
    if stop_sec > 0:
        stop_timer = windows.after(1000, stop_sec_count_down, stop_sec - 1)
        stop_sec -= 1
        print(stop_sec)
    elif stop_sec == 0:
        entry.delete("1.0", END)
        entry.config(state=DISABLED)
        windows.after_cancel(session_timer)
        time_text.config(text=session_time)
        windows.update()


# This function restarts the stop_sec_count_down function each time the user hits on a key on the keyboard
def is_writing(event):
    global stop_timer
    windows.after_cancel(stop_timer)
    stop_sec_count_down(stop_sec)


windows = Tk()
windows.title("The most dangerous writing app")
windows.minsize(width=400, height=300)
# We bind the is_writing function to the tkinter window so that everything is lost when the user stops typing
windows.bind("<Key>", is_writing)

heading = Label(text="Dont stop writing, or all your progress will be lost.", padx=20, font=("Arial", 22, 'italic'))
heading.grid(column=0, row=0, columnspan=4, padx=250, pady=20)

time_left = Label(text="Session Time:", font=Font)
time_left.grid(column=1, row=2, pady=0, columnspan=2)

time_text = Label(text=session_time, font=Font)
time_text.grid(column=1, row=3, pady=0, columnspan=2)

entry = Text(windows, width=120, height=20, state=DISABLED)
entry.grid(column=1, row=4, columnspan=2, pady=20)

start_button = Button(text="Start", width=10, font='/', background="red", foreground="white", command=start)
start_button.grid(column=1, row=5, columnspan=2, pady=20)

windows.mainloop()













# import tkinter as tk
# import random

# COLORS =["red", "orange", "yellow", "green", "blue", "violet"]

# class Application(tk.Frame): 

#     def __init__(self,master):
#         self.master = master
#         tk.Frame.__init__(self)
#         self.pack()

#         self._after_id = None
#         self.entry = tk.Entry(self)
#         self.entry.pack()
#         self.entry.bind('<Key>',self.handle_wait)

#     def handle_wait(self,event):
#         # cancel the old job
#         if self._after_id is not None:
#             self.after_cancel(self._after_id)

#         # create a new job
#         self._after_id = self.after(1000, self.change_color)

#     def change_color(self):
#         random_color = random.choice(COLORS)
#         self.entry.config(background=random_color)

# root = tk.Tk()
# app = Application(root)
# app.mainloop()





# import tkinter as tk
# import random

# COLORS =["red", "orange", "yellow", "green", "blue", "violet"]

# class Application(tk.Frame): 

#     def __init__(self,master):
#         self.counter = 0
#         self.master = master
#         tk.Frame.__init__(self)
#         self.pack()

#         self.entry = tk.Entry(self)
#         self.entry.pack()
#         self.entry.bind('<Key>',lambda event: self.handle_wait(event))


#     def handle_wait(self,event):
#         self.counter += 1
#         counter = self.counter
#         self.after(1000,lambda: self.handle_wait2(counter) )


#     def handle_wait2(self,counter):
#         if self.counter == counter:
#             self.change_color()

#     def change_color(self):
#         random_color = random.choice(COLORS)
#         self.entry.config(background=random_color)

# root = tk.Tk()
# app = Application(root)
# app.mainloop()