from .schemas.invalid_response import InvalidResponseSchema


class AlertException(Exception):
    """
    Alert Exception for API
    """

    def __init__(self, response: InvalidResponseSchema | None = None):
        if not response:
            return super().__init__()
        self.response = response
        self.message = self.get_message(self.response)

        super().__init__(self.message)

    def get_message(self, response: InvalidResponseSchema):
        pass
