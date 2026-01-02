# WEB IMAGE DOWNLOADER

This is a simple python app to download images from a specified website.

All you need to run this app is python 3.8 or higher, and install all the dependencies listed in requirements.txt + having TkInter downloaded in your system. For the execution you just need to run the app.py file.

# Installation

First, clone this repository inside a folder in your computer
```
git clone https://github.com/aperezmarquez/web-img-downloader
```
DOnce you clone the repo, download all the dependencies from the root folder with:
```
pip install -r requirements.txt
```

Check if you have TkInter installed. If you run the next command it should open a tiny window if TkInter is correctly installed.
```
python -m tkinter
```
In case it doesn't, install it. If you are using an Unix distribution, run the next commands.
```
sudo apt update
sudo apt install python3-tk
```

# Execution

Run the following command inside the root folder to run the app.
```
python app.py
```

Once you run it a window will open and you can start downloading the images. To do so insert the URL of the page you want to download the images from and click on the Download button. This will start the process and they will start popping inside the list in left hand side of the window. When you have downloaded all the images, you can check them inside the assets folder.
