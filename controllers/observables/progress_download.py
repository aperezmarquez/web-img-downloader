from rx.subject import Subject

# SUBJECT FOR THE SELECTED IMAGE
# - Params:
#   - max: the max value of the progress bar
# - Functions:
#   - subscribe: returns the subject subscription
#   - update_progress: updates the progress value and notifies the observers
#   - get_max: returns the max value of the progress bar
# - Description: Subject for the progress of the download to show visually to the user
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
