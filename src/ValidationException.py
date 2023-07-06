class ValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# custom class that extends 'Exception' base class
# takes only 1 parameter - message
# line 4 invokes the __init__ of the 'Exception class
