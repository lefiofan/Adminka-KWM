from typing import Optional
from ninja import Schema, ModelSchema
from markirovka.schemas.tara import tara_all
from markirovka.models import Product

class products_all2(Schema):
    class Config:
        orm_mode = True
    id: int
    title: str
    img: Optional[str]
    gtin: str
    tara: Optional[tara_all]

class products_all(ModelSchema):
    class Config:
        model = Product
        model_fields = "__all__"

class products_add(ModelSchema):
    class Config:
        model = Product
        model_exclude = ['id', 'created']

class products(ModelSchema):
    class Config:
        model = Product
        model_exclude = ['id']