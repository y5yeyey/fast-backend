from enum import Enum
from typing import Optional

from pydantic import BaseModel

class ModelType(str, Enum):
    invalid = "invalid"
    supply = "supply"
    demand = "demand"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    id: int
    type: ModelType
    price: float
