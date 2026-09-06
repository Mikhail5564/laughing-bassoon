from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    count: int
    price: float


products: list[Product] = []


TOTAL_TICKETS = 100

@dataclass
class Member:
    id: int
    first_name: str
    last_name: str
    age: int


members: list[Member] = []


ivan_votes = 6
mikhail_votes = 4


def percent(golos, total_golos):
    return (golos / total_golos) * 100


