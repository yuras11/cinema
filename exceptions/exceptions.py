class AppException(Exception):
    def __init__(self, message: str = 'Application error'):
        self.__message = message
        super().__init__(message)

    def get_message(self):
        return self.__message


class NotFoundException(AppException):
    pass


class AlreadyExistsException(AppException):
    pass