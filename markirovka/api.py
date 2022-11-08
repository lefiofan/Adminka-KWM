from typing import List
from ninja.security import django_auth
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from markirovka.models import Tara
from markirovka.schema import tara_all, tara_add

api = NinjaAPI(title='API Мин Вода',auth=django_auth, csrf=True)


from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}


@api.post("/tara", auth=django_auth, tags=["Тара"], description="Метод добаления тар", summary="Метод добаления тар")
def create_tara(request, payload: tara_add):
    tara = Tara.objects.create(**payload.dict())
    return {"id": tara.id}

# Получить все тары
@api.get("/tara", response=List[tara_all], tags=["Тара"], description="Выводит список тар", summary="Выводит список тар")
def get_all(request):
    return Tara.objects.all()

# Получить тару по названию
@api.get("/tara/{obiem}", response=tara_all, summary="Обьем тары", description="Выводит подробную информацию по таре", auth=django_auth, tags=["Тара"])
def get_in_name(request, obiem: str):
    return get_object_or_404(Tara, name=obiem)

@api.put("/tara/{tara_id}", auth=django_auth, tags=["Тара"], summary="Метод редактирования тар", description="Метод редактирования тар")
def update_employee(request, tara_id: int, payload: tara_add):
    tara = get_object_or_404(Tara, id=tara_id)
    for attr, value in payload.dict().items():
        setattr(tara, attr, value)
    tara.save()
    return {"success": True}


@api.delete("/tara/{tara_id}", auth=django_auth, tags=["Тара"], summary="Метод удаления тар", description="Метод удаления тар")
def delete_employee(request, tara_id: int):
    tara = get_object_or_404(Tara, id=tara_id)
    tara.delete()
    return {"success": True}