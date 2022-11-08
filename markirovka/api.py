from ninja.security import django_auth
from ninja import NinjaAPI
from markirovka.api_routes.tara import router as taras_routers
from markirovka.api_routes.country import router as country_routers

api = NinjaAPI(title='API Мин Вода',auth=django_auth, csrf=True)

api.add_router("/tara/", taras_routers)
api.add_router("/country/", country_routers, tags=["Страна"])