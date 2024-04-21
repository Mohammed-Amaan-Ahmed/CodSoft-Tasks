import tkinter as tk
def add_task():
  task = entry.get()
  if task != "":
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
def remove_task():
  selected = listbox.curselection()
  if selected:
    listbox.delete(selected[0])
window = tk.Tk()
window.title("To-Do List")
label = tk.Label(window, text="Enter a new task:")
label.pack()
entry = tk.Entry(window)
entry.pack()
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()
listbox = tk.Listbox(window)
listbox.pack()
remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack()
window.mainloop()
