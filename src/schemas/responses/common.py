from pydantic import BaseModel


class PingPongResponse(BaseModel):
    ping: str = 'pong!'
