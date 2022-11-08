from ninja import Schema

class tara_all(Schema):
    id: int
    name: str

class tara_add(Schema):
    name: str