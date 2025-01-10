from dataclasses import dataclass
from token import OP
from typing import Optional


@dataclass
class State:
    backend_url: Optional[str] = None
