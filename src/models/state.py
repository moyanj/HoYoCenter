from dataclasses import dataclass
from typing import Optional


@dataclass
class State:
    backend_url: Optional[str] = None
