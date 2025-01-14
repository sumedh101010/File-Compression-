import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog #file dialog used to select any file from the pc

def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title="select a file to compress")
    return filename

def compression(i,o):
    compress(i,o) 

window=tk.Tk()
window.title("compression engine")
window.geometry("600x400")
 
compress_button=tk.Button(window,text="compress",command=lambda:compression(open_file(),"compressed_output1.txt")) 
compress_button.grid(row=2,column=1)
window.mainloop()