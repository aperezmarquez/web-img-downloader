from rx.subject import BehaviorSubject
from PIL import Image

# SUBJECT FOR THE SELECTED IMAGE
# - Params:
#   - image: the selected image name
# - Functions:
#   - subscribe: returns the subject subscription
#   - change_img: updates the image and notifies the observers
# - Description: Subject for the image selection shown in the TkInter window
class ImageSubject:
    def __init__(self, image):
        self.image = Image.open(image)
        self.subject = BehaviorSubject(self.image)
        super().__init__()

    def subscribe(self, observer):
        return self.subject.subscribe(observer)

    def change_img(self, new_img):
        if self.image == new_img:
            return
        
        self.image = new_img
        self.subject.on_next(new_img)
