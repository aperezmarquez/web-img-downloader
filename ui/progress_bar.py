from tkinter import ttk

progressbar = None
btn = None

# SUBSCRIBE TO THE PROGRESS SUBJECT
# - Params:
#   - progress_sub: the progress subject to subscribe
# - Return: None
# - Description: Subscribes to the progress subject and updates the progress bar
def update_progress_sub(progress_sub):
    global progressbar
    progressbar["maximum"] = progress_sub.get_max()
    progress_sub.subscribe(lambda v: change_progress(v))
    btn["state"] = "disabled"

# ENABLES THE DOWNLOAD BUTTON
# - Params: None
# - Return: None
# - Description: Enables the download button
def enable_btn():
    global btn
    btn["state"] = "normal"

# UPDATES THE PROGRESS BAR
# - Params:
#   - value: the new value for the progress bar
# - Return: None
# - Description: Updates the progress bar
def change_progress(value):
    global progressbar
    progressbar["value"] = progressbar["maximum"] - value

    # If the download is done the download button is ready to use again
    if progressbar["value"] == progressbar["maximum"]:
        enable_btn()

# PROGRESS BAR TO SHOW THE DOWNLOAD PROGRESS
# - Params:
#   - root: the window root
#   - button: the button that starts the download
# - Description: Creates the progress bar
def progress_bar(root, button):
    global progressbar, btn
    btn = button
    progressbar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progressbar.pack(pady=10)

