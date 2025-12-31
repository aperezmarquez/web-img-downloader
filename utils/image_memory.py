memory_images = {}

def get_images():
    global memory_images
    return memory_images

def add_image(name, img):
    global memory_images
    memory_images[name] = img
