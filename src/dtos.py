# dtos.py

from pydantic import BaseModel


class PathDTO(BaseModel):
    path: str
