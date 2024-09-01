import tkinter as tk
from tkinter import messagebox

class MyGui():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple GUI")
        self.root.geometry("600x300")

        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 14))
        self.label.pack(padx=20, pady=10)
        
        self.menu = tk.Menu(self.root)  # Create a menu (drop down type)
        self.fileMenu = tk.Menu(self.menu, tearoff=0) # Create a menu items ,tearoff is used to remove the dashed line from the beginning of (index = -1) from  menu

        self.fileMenu.add_command(label="close", command=exit) # Add a menu item to the menu
        self.fileMenu.add_separator() # Add a separator to the menu
        self.fileMenu.add_command(label="New" , command=self.show_message ) # Add a menu item to the menu
        
        self.actionmenu = tk.Menu(self.menu, tearoff=0) # Create a menu items ,tearoff is used to remove the dashed line from the beginning of (index = -1) from  menu
        self.actionmenu.add_command(label="show message", command=self.show_message)

        self.menu.add_cascade(label="actions", menu=self.actionmenu) # add_cascade is used to add all the menu items to the menu
        self.menu.add_cascade(label="files", menu=self.fileMenu) # add_cascade is used to add all the menu items to the menu

        self.root.config(menu=self.menu) # Set the menu to the root window

        self.textArea = tk.Text(self.root, height=3)
        self.textArea.bind("<KeyPress>", self.create_shortcut)
        self.textArea.pack(padx=20, pady=20)

        self.check_state = tk.IntVar()

        self.checkbtn = tk.Checkbutton(self.root, text="show message", variable=self.check_state)
        self.checkbtn.pack(padx=5, pady=5)

        self.button = tk.Button(self.root, text="Click Me", command=self.show_message)
        self.button.pack(padx=5, pady=5)    

        self.btn = tk.Button(self.root, text="clear", command=self.clear_text)
        self.btn.pack(padx=5, pady=5)

        # self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        self.root.protocol("WM_DELETE_WINDOW", self.closeUi)  # This will call the closeUi method when the close button (WM_delete_window) is clicked
        self.root.mainloop()

    def show_message(self):
        if(self.check_state.get()==0):
            print(self.textArea.get("1.0", tk.END))
        else:
            messagebox.showinfo("Message",self.textArea.get("1.0",tk.END))
            # messagebox.showerror("Error","This is an error message")    
            #self.textArea.get("1.0",tk.END) this means get the text from the first line to the end of the text in the textArea. 

    def create_shortcut(self, event):
         if event.state & 0x0004 and event.keysym == "Return":  # 0x0004 is the state for Control key == 8
            print(f"Key Pressed: {event.keysym}, State: {event.state}")
            self.show_message()

    def closeUi(self):
        if (messagebox.askyesno("Quit", "Do you want to quit?")):
            self.root.destroy()

    def clear_text(self):
        self.textArea.delete("1.0", tk.END)

MyGui()
