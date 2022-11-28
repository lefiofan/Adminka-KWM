from markirovka.models import Donwload_codes
from markirovka.schemas.consumer_codes import consumer_codes_by_country, consumer_codes_all
from typing import List
from ninja.security import django_auth
from ninja import Router

router = Router()

@router.get("/{country_id}", response=List[consumer_codes_by_country], summary="Получить все коды по стране и продукту",
            description="Выводит подробную информацию о кодах по стране и продукту", auth=django_auth)
def get_in_name(request, country_id: int, products_id: int):
    codes = Donwload_codes.objects.filter(country__id=country_id).filter(products__id=products_id).all()
    data = [consumer_codes_by_country.from_orm(i).dict() for i in codes]
    return data

