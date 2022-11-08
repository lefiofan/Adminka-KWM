from ninja import Schema

class country_all(Schema):
    id: int
    name: str

class country_add(Schema):
    name: str