import tkinter
import tkinter.ttk as ttk
pen = tkinter.Tk()
btn = ttk.Button(text='Terminale "Merhaba" Yaz', command=lambda: print('Merhaba'))
btn.pack(padx=50, pady=50)
pen.mainloop()
