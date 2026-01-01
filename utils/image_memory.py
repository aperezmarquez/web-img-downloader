memory_images = {}

# GET IMAGES
# - Params: None
# - Return:
#   - memory_images: the images saved in memory
# - Description: Gets the images saved in memory
def get_images():
    global memory_images
    return memory_images

# ADD IMAGE
# - Params:
#   - name: new image name being added
#   - img: the image itself
# - Return: None
# - Description: Adds the image in memory referencing it by its name
def add_image(name, img):
    global memory_images
    memory_images[name] = img
