from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    count: int
    price: float


products: list[Product] = []