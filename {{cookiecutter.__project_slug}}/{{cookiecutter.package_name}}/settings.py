import os
from dataclasses import dataclass


@dataclass
class Settings:
    multiplier_factor: float

    @classmethod
    def build(cls) -> "Settings":
        """Build app settings dynamically, if needed."""
        return cls(multiplier_factor=float(os.getenv("MULTIPLIER_FACTOR", 1.0)))
