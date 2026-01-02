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
python main.py
```

Once you run it a window will open and you can start downloading the images. To do so insert the URL of the page you want to download the images from and click on the Download button. This will start the process and they will start popping inside the list in left hand side of the window. When you have downloaded all the images, you can check them inside the assets folder.

# How does it work?

When executing the main.py file, a root Tkinter window is created. At the same time, an asyncio event loop is started and integrated with Tkinter using the **after** method, which executes the loop every 10 ms. This approach allows asynchronous tasks to run without blocking the graphical user interface and without using threads.

Once the event loop is running, the main application window is created. This window contains the following components:

## Main Components

- **Listbox**  
  Displays one entry per downloaded image. The list is updated dynamically every time a new image is downloaded. This is achieved using a reactivex.Subject that emits the image name (obtained from the alt attribute of the `<img>` tag or from the image URL) once a download asyncio task is completed.

- **Image Viewer**  
  When the user selects an item from the list, the corresponding image is displayed on the right side of the window. This behavior is implemented using another reactivex.Subject, which emits the selected image data stored in memory and updates the PIL.ImageTk.PhotoImage shown in the UI.

- **Progress Bar**  
  Shows the progress of the image download process. Each completed image download triggers an update through a reactivex.Subject connected to the number of pending images.

## Asynchronous and Reactive Architecture

All images are downloaded concurrently using asyncio and aiohttp, and their binary data is kept entirely in memory (never written to disk). The application follows the Observable–Observer pattern provided by Reactivex, which cleanly decouples the asynchronous download logic from the graphical user interface.

This design ensures that:
- The UI remains responsive at all times
- There are no deadlocks or race conditions
- No threads are used; concurrency is handled exclusively with asyncio

