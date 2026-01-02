from rx.subject import Subject

class ProgressSubject:
    def __init__(self, max):
        self.subject = Subject()
        self.progress = 0
        self.max = max
        super().__init__()

    def subscribe(self, observer):
        return self.subject.subscribe(observer)

    def update_progress(self, value):
        self.progress = value
        self.subject.on_next(self.progress)

    def get_max(self):
        return self.max
