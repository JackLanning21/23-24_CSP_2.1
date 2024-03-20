#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("500x500")

frame_login = tk.Frame(root)
frame_login.grid()


lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=175)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

btn_login = tk.Label(frame_login, text='Login:')
btn_login.pack(pady=5)

tk.Label(frame_login,text="Password:",font="Courier")
root.mainloop()
