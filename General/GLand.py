from dataclasses import dataclass


@dataclass
class GLand:
    name: str

    def __hash__(self):
        return hash(self.name)