class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class PhoneFormatError(Error):
    """Raised error if give phone number format is invalid"""
    def __init__(self, message='Wrong phone number format!'):
        self.message = message
