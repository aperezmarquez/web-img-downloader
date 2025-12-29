from rx.subject import BehaviorSubject

class ImageSubject:
    def __init__(self, image):
        self.image = image
        self.subject = BehaviorSubject(image)
        super().__init__()

    def subscribe(self, observer):
        return self.subject.subscribe(observer)

    def change_img(self, new_img):
        if self.image == new_img:
            return
        
        self.image = new_img
        self.subject.on_next(new_img)
