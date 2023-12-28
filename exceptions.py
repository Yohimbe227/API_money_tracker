class Error(Exception):
    pass


class TokenError(Error):
    def __init__(self, token):
        self.token = token
        super().__init__(f"Отсутствует необходимый токен: {token}")
