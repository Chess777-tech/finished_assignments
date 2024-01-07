import tkinter as tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename  # We use to pop opne save as/ open as 



def open_file(window,text_edit):
    filepath = askopenfilename(filetypes=[("Text Files","*.txt")])   # *.txt  extension for calling the file 

    if not filepath:
        return
    
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window,text_edit):
    filepath=  asksaveasfilename(filetypes=[("Text Files","*.txt")]) 
    if not filepath:
        return
    
    with open(filepath, "w") as f:  # this will overwite existing file
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File {filepath}")


def test():
    print("run")

def main():
    window = tk.Tk()
    window.title("Text editor")
    window.columnconfigure(1, minsize=500)
    window.rowconfigure(0, minsize=400)
    
    
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row = 0, column= 1)

    frame = tk.Frame(window, relief=tk.RAISED, bd =2 )
    save_button = tk.Button(frame, text="Save",command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))  # a function that calls the function with the arguements that we need

    save_button.grid(row=0, column=0, padx=5, pady=5)
    open_button.grid(row=1, column=0,padx=5, sticky="ew") #sticky allows us to expand east and west
    frame.grid(row=0, column=0, sticky="ns") #ns expands the frame to the east or west of windwow


    window.bind("<Control-s>", lambda x: save_file(window,text_edit))    #lambda as calls whatever function with a single arguement.... needs one arguement 
    window.bind("<Control-o>", lambda x: open_file(window,text_edit))  
    window.mainloop()


main()
