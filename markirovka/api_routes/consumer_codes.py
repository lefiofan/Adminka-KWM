from markirovka.models import Donwload_codes
from markirovka.schemas.consumer_codes import consumer_codes_by_country, consumer_codes_all
from typing import List
from ninja.security import django_auth
from ninja import Router

router = Router()

@router.get("/{country_id}", response=List[consumer_codes_by_country], summary="Получить все коды по стране",
            description="Выводит подробную информацию о кодах по стране", auth=django_auth)
def get_in_name(request, country_id: int, products_id: int):
    codes = Donwload_codes.objects.filter(country__id=country_id).filter(products__id=products_id).all()

    data = [consumer_codes_by_country.from_orm(i).dict() for i in codes]
    return data

# @router.get("/{obiem}", response=products_all2, summary="Получить продукты по ID тары", description="Выводит подробную информацию о продуктах по id тары", auth=django_auth)
# def get_in_tara_id(request, obiem: str):
#     return get_object_or_404(Product, tara_id=obiem)
# # Получить все продукты
@router.get("/", response=List[consumer_codes_all], description="Выводит список продуктов", summary="Выводит список продуктов")
def get_all(request):
    return Donwload_codes.objects.all()
#
# @router.put("/update/{product_id}", auth=django_auth,  summary="Метод редактирования тар", description="Метод редактирования тар")
# def update_products(request, product_id: int, payload: products_add):
#     product = get_object_or_404(Product, id=product_id)
#     for attr, value in payload.dict().items():
#         setattr(product, attr, value)
#     product.save()
#     return {"success": True}
#
# @router.delete("/delete/{product_id}", auth=django_auth, summary="Метод удаления продукта", description="Метод удаления продукта")
# def delete_tara(request, product_id: int):
#     product = get_object_or_404(Product, id=product_id)
#     product.delete()
#     return {"success": True}