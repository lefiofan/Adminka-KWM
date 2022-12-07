from markirovka.models import Korob, Donwload_codes_korob
from markirovka.schemas.korob import output_box_by_code
from typing import List
from ninja.security import django_auth
from ninja import Router

router = Router()

@router.get("/{group_codes}", response=output_box_by_code,  summary="Получить информацию о ящике",
            description="Получить информацию о ящике по групповому коду", auth=django_auth)
def get_in_group_codes(request, group_codes: int):
    group_codes_id_from_db = Donwload_codes_korob.objects.filter(code=group_codes).get().id

    group_codes_in_db = Korob.objects.get(korob_code_id=group_codes_id_from_db)
    products_codes = Korob.objects.get(korob_code_id=group_codes_id_from_db).products_code.all()
    products_codes_list = []

    for cod in products_codes:
        products_codes_list.append(cod.code)


    #data = [consumer_codes_by_country.from_orm(i).dict() for i in codes]
    return output_box_by_code(id=group_codes_in_db.id, group_codes=str(group_codes_in_db.korob_code), products_codes=products_codes_list, aggr=group_codes_in_db.aggr, nanes=group_codes_in_db.nanes)

