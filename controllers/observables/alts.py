from rx.subject import Subject

# SUBJECT FOR IMAGE NAMES/ALTS
# - Params: None
# - Functions:
#   - subscribe: returns the subject subscription
#   - add_alt: adds a new alt to the subject and notifies the observers of the new added name
#   - get_alts: returns the list of alts/names
# - Description: Subject for the image names/alts
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

