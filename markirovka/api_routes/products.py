from markirovka.models import Product
from markirovka.schemas.products import products_all, products_add, products_all2
from django.shortcuts import get_object_or_404
from typing import List
from ninja.security import django_auth
from ninja import Router

router = Router()

@router.get("/{name}", response=products_all2, summary="Получить продукты по названию", description="Выводит подробную информацию о продуктах по названию", auth=django_auth)
def get_in_name(request, name: str):
    return get_object_or_404(Product, title=name)

@router.get("/dd/{obiem}", response=products_all2, summary="Получить продукты по ID тары", description="Выводит подробную информацию о продуктах по id тары", auth=django_auth)
def get_in_tara_id(request, obiem: int):
    return get_object_or_404(Product, tara_id=obiem)

# Получить все продукты
@router.get("/", response=List[products_all2], description="Выводит список продуктов", summary="Выводит список продуктов")
def get_all(request):
    return Product.objects.all()

@router.put("/update/{product_id}", auth=django_auth,  summary="Метод редактирования тар", description="Метод редактирования тар")
def update_products(request, product_id: int, payload: products_add):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}

@router.delete("/delete/{product_id}", auth=django_auth, summary="Метод удаления продукта", description="Метод удаления продукта")
def delete_tara(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}