import tkinter as tk
from tkinter import messagebox
import pyautogui
import datetime
import time

def take_screenshot():
    
    root.withdraw() 
    
    time.sleep(0.5) 
    
    img = pyautogui.screenshot()
    
    time_now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Jenil_Shot_{time_now}.png"
    
    img.save(filename)
    
    root.deiconify() 
    
    messagebox.showinfo("Success! 🎉", f"Screenshot saved as:\n{filename}")

root = tk.Tk()
root.title("Jenil's Screen Capturer")
root.geometry("300x200")
root.configure(bg='#0f172a')

root.attributes('-topmost', True) 

tk.Label(root, text="📸 SNAP STUDIO", font=("Courier", 20, "bold"), bg='#0f172a', fg='#38bdf8').pack(pady=25)

snap_btn = tk.Button(root, text="TAKE SCREENSHOT", font=("Arial", 12, "bold"),bg='#ef4444', fg='white', bd=0, padx=15, pady=8, command=take_screenshot)
snap_btn.pack()

root.mainloop()
