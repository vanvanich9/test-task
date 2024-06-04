import fastapi


class HTTPBadRequest(fastapi.HTTPException):
    def __init__(self, detail: str = "Bad request."):
        super().__init__(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )


class HTTPNotFound(fastapi.HTTPException):
    def __init__(self, detail: str = "Not found."):
        super().__init__(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=detail,
        )
