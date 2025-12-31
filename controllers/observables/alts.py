from rx.subject import BehaviorSubject

class AltsSubject:
    def __init__(self):
        self.alts = []
        self.n_alts = 0
        self.subject = BehaviorSubject(self.alts)
        super().__init__()

    def subscribe(self, observer):
        return self.subject.subscribe(observer)

    def add_alt(self, alt):
        self.alts.append(alt)
        self.n_alts += 1
        self.subject.on_next(self.alts[self.n_alts - 1])
