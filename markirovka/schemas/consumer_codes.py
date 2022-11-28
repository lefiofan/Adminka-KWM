from typing import Optional
from ninja import Schema, ModelSchema

from markirovka.schemas.country import country_all
from markirovka.schemas.products import products_all
from markirovka.models import Donwload_codes

class consumer_codes_by_country(Schema):
    class Config:
        orm_mode = True
    id: int
    code: str
    aggr: bool
    nanes: bool

class consumer_codes_all(ModelSchema):
    class Config:
        model = Donwload_codes
        model_fields = "__all__"

# class products_add(ModelSchema):
#     class Config:
#         model = Product
#         model_exclude = ['id', 'created']
#
# class products(ModelSchema):
#     class Config:
#         model = Product
#         model_exclude = ['id']