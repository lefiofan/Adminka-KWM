from typing import Optional, List

from ninja import Schema


class output_box_by_code(Schema):
    class Config:
        orm_mode = True
    id: int
    group_codes: str
    products_codes: List[str]
    aggr: bool
    nanes: bool