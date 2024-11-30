import tkinter as tk

class Application(tk.Frame): 

    def __init__(self,master):
        self.master = master
        self.master.title("VANISH🔮")
        tk.Frame.__init__(self)
        self.pack()


        self._after_id = None
        self.entry = tk.Text(self,height=40, width=40,font=('Times New Roman', 25, 'bold'),)
        self.entry.grid(column=0,row=0)
        self.entry.bind('<Key>',self.handle_wait)


    def handle_wait(self,event):
        # cancel the old job
        if self._after_id is not None:
            self.after_cancel(self._after_id)

        # create a new job
        self._after_id = self.after(1000*5, self.delete_entry)

    def delete_entry(self):
        self.entry.delete("1.0","end")

root = tk.Tk()
app = Application(root)
app.mainloop()





















# from tkinter import *







# window =Tk()
# window.title('VANISH')
# window.minsize(600,500)

# text_entry=Text(height=40, width=40,font=('Times New Roman', 25, 'bold'))
# text_entry.grid(column=0,row=0)



# window.mainloop()