from ui.window import window
import tkinter as tk
import asyncio

WIDTH = 1400
HEIGHT = 800

if __name__ == "__main__":
    root = tk.Tk()
    
    # Asyncio event loop that runs in the background at the same time as the UI
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    def poll_asyncio():
        loop.stop()
        loop.run_forever()
        root.after(10, poll_asyncio)
    
    # Starts the event loop and runs it every 10ms, stopping the older one
    poll_asyncio()
    
    # Creates the window app with all the elements
    window(root, WIDTH, HEIGHT, loop)

    root.mainloop()
