from http import HTTPStatus
from typing import Any

from pydantic import BaseModel


class Response(BaseModel):
    status: HTTPStatus
    body: Any
