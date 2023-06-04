from dataclasses import dataclass


@dataclass
class Cell:
    x: int
    y: int
    alive: bool = True
