from rx.subject import Subject

class AltsSubject:
    def __init__(self):
        self.alts = []
        self.subject = Subject()

    def subscribe(self, observer):
        return self.subject.subscribe(observer)

    def add_alt(self, alt):
        self.alts.append(alt)
        self.subject.on_next(alt)

    def get_alts(self):
        return self.alts

