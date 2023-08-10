import tkinter as tk

window = tk.Tk()

label = tk.Label(text="IMAGE AUTH").pack()
set_image_passcode = tk.Button(
        text="Set Imgcode",
        width=25,
        height=25
        ).pack()
unlock_with_image_passcode = tk.Button(
        text="Unlock with Imgcode",
        width=25,
        height=25
        ).pack()

window.mainloop()
