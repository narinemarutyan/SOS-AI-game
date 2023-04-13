from dataclasses import dataclass

from location import Location
from sign import Sign


@dataclass
class Move:
    location: Location
    sign: Sign
