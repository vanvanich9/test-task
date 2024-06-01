import fastapi


class HTTPBadRequest(fastapi.HTTPException):
    def __init__(self):
        super().__init__(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail="Bad request.",
        )
