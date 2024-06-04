from http import HTTPStatus
from typing import Any

from pydantic import BaseModel


class Request(BaseModel):
    params: dict | None = None
    headers: dict | None = None
    cookies: dict | None = None
    files: list[dict] | None = None
    body: dict | None = None


class Response(BaseModel):
    status: HTTPStatus
    body: Any
