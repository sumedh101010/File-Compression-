import tkinter as tk
from compressmodule import compress,decompress
def compression(i,o):
    compress(i,o)

  
window=tk.Tk()
window.title("compression engine")
window.geometry("600x400")   #x ayega idhar 

input_entry=tk.Entry(window)  # this only creates the entries in doesnt add it to the window to add it use grid, entry means blank space where user writes 
output_entry=tk.Entry(window)  # this only creates the entries in doesnt add it to the window to add it use grid 

input_label=tk.Label(window,text="file to be compressed")  # label writes the heading or text in the tkinter window 
output_label=tk.Label(window,text="name of the compressed file ")

input_label.grid(row=0,column=0)

compress_button=tk.Button(window,text="compress",command=lambda:compression(input_entry.get(),output_entry.get())) # lambda function used because its more dynamic and when the user enters value it fetches the real time value from input field s

input_entry.grid(row=0,column=1)  #decides where the blank space will be there for user user to enter the input
output_label.grid(row=1,column=0)
output_entry.grid(row=1,column=1)

compress_button.grid(row=2,column=1)
window.mainloop()