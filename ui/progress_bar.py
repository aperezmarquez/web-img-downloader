from tkinter import ttk

progressbar = None

def update_progress_sub(progress_sub):
    global progressbar
    progressbar["maximum"] = progress_sub.get_max()
    progress_sub.subscribe(lambda v: change_progress(v))

def change_progress(value):
    global progressbar
    progressbar["value"] = progressbar["maximum"] - value

def progress_bar(root):
    global progressbar
    progressbar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progressbar.pack(pady=10)

