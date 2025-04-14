from pydantic import BaseModel, field_validator
from typing import Union

class DistanciaInput(BaseModel):
    origem: Union[str, int]
    destino: Union[str, int]

    @field_validator('origem', 'destino', mode='before')
    @classmethod
    def to_string(cls, v):
        return str(v)

class DistanciaOutput(BaseModel):
    distancia_km: float

class ErrorSchema(BaseModel):
    message: str
