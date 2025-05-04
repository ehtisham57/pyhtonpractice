import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

win = tk.Tk()
win.title("Calculator")
win.geometry("300x400")

entry = tk.Entry(win, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(win)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", width=5)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

win.mainloop()
