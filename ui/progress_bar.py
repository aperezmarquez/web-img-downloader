from tkinter import ttk

progressbar = None
btn = None

def update_progress_sub(progress_sub):
    global progressbar
    progressbar["maximum"] = progress_sub.get_max()
    progress_sub.subscribe(lambda v: change_progress(v))
    btn["state"] = "disabled"

def enable_btn():
    global btn
    btn["state"] = "normal"

def change_progress(value):
    global progressbar
    progressbar["value"] = progressbar["maximum"] - value

    if progressbar["value"] == progressbar["maximum"]:
        enable_btn()

def progress_bar(root, button):
    global progressbar, btn
    btn = button
    progressbar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progressbar.pack(pady=10)

