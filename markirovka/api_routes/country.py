from markirovka.models import Country
from markirovka.schemas.country import country_all, country_add
from django.shortcuts import get_object_or_404
from typing import List
from ninja.security import django_auth
from ninja import Router

router = Router()

@router.post("/", auth=django_auth, description="Метод добаления страны", summary="Метод добаления страны")
def create_country(request, payload: country_add):
    country = Country.objects.create(**payload.dict())
    return {"id": country.id}

# Получить все страны
@router.get("/", response=List[country_all],  description="Выводит список стран", summary="Выводит список стран")
def get_all(request):
    return Country.objects.all()

@router.put("/{tara_id}", auth=django_auth, summary="Метод редактирования тар", description="Метод редактирования тар")
def update_country(request, tara_id: int, payload: country_add):
    country = get_object_or_404(Country, id=tara_id)
    for attr, value in payload.dict().items():
        setattr(country, attr, value)
    country.save()
    return {"success": True}

@router.delete("/{tara_id}", auth=django_auth,  summary="Метод удаления тар", description="Метод удаления тар")
def delete_country(request, tara_id: int):
    country = get_object_or_404(Country, id=tara_id)
    country.delete()
    return {"success": True}