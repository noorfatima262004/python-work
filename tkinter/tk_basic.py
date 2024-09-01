import tkinter as tk

root = tk.Tk()

root.title("My first GUI")
root.geometry("500x500")

lable = tk.Label(root, text="Hello World", fg="red", font=("Arial", 40))
# lable.pack(padx=20, pady=20)
# lable.place(x=100, y=100)


# Place Usage: Allows for precise, manual placement of widgets using absolute or relative coordinates.
# place Usage: Places widgets at a specific x,y coordinate. This is useful for precise placement of widgets.
# pack Usage: Places widgets in a block format. This is useful for simple layouts.
# Usage: Automatically arranges widgets within the window based on the order they are packed.
# Positioning: Widgets are placed sequentially in a stacked manner, either vertically or horizontally. You can control their placement relative to sides (top, bottom, left, right), but not the exact coordinates.
# grid Usage: Places widgets in a grid format. This is useful for complex layouts.


label1 = tk.Label(root, text="Label 1")
# label1.pack(side='right',padx=10, pady=10)
label1.pack(side='right', anchor='n' , padx=10, pady=10)  # Align to the top-right corner


label2 = tk.Label(root, text="Label 2")
label2.pack(padx=10, pady=10)

label3 = tk.Label(root, text="Label 3")
label3.pack( padx=10, pady=10)

textArea = tk.Text(root, height=3)  # Multi-line text input
# Place textArea at the top using the 'before' option
textArea.pack( padx=10, pady=10, before=label1)

textLine = tk.Entry(root) #entry is used for input fields for just one line u can use it for password fields and can not be used for multiline text.
textLine.pack()  

button = tk.Button(root, text="Click Me", command=lambda: print("Button Clicked"))
button.pack( padx=10, pady=10)

buttonFram = tk.Frame(root)
buttonFram.columnconfigure(0, weight=1)
buttonFram.columnconfigure(1, weight=1)
buttonFram.columnconfigure(2, weight=1)

button1 = tk.Button(buttonFram, text="Button 1")
button1.grid(row=0, column=0, sticky=tk.W+tk.E)

button2 = tk.Button(buttonFram, text="Button 2")
button2.grid(row=0, column=1, sticky=tk.W+tk.E)

button3 = tk.Button(buttonFram, text="Button 3")
button3.grid(row=0, column=2, sticky=tk.W+tk.E)

button4 = tk.Button(buttonFram, text="Button 4")
button4.grid(row=1, column=0, sticky=tk.W+tk.E)

button5 = tk.Button(buttonFram, text="Button 5")
button5.grid(row=1, column=1, sticky=tk.W+tk.E)

buttonFram.pack(fill='x')  # fills / expands the button in x (hori) direction

#The sticky option in Tkinter’s grid() method is used to control how the widget "sticks" or stretches within its grid cell. It determines which sides of the cell the widget should be aligned to or stretched towards. The values used for sticky represent the cardinal directions: north (N), south (S), east (E), and west (W).

#sticky=tk.W: The widget will align to the left (west) side of the cell.
# sticky=tk.E: The widget will align to the right (east) side of the cell.
# sticky=tk.N+tk.S+tk.W+tk.E: The widget will stretch to fill the entire cell both horizontally and vertically.
#tk.W+tk.E: This means the widget should stick to both the west (left) and east (right) sides of the cell. It makes the widget stretch horizontally to fill the entire width of the grid cell, but not vertically.

btn = tk.Button(root, text="Click btn", command=lambda: print("Button Clicked place command used"))
btn.place(x=200, y=200)  # Place the button at the specified x, y coordinates

root.mainloop()

#  Tkinter doesn't allow mixing pack() and grid() in the same window (or frame) without causing layout issues.
# Ensure that all widgets in the same container (root) use the same geometry manager (grid() or pack()).