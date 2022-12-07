from ninja.security import django_auth
from ninja import NinjaAPI
from markirovka.api_routes.tara import router as taras_routers
from markirovka.api_routes.country import router as country_routers
from markirovka.api_routes.products import router as products_routers
from markirovka.api_routes.group_codes import router as group_codes_routers
from markirovka.api_routes.consumer_codes import router as consumer_codes_routers
from markirovka.api_routes.korob import router as korob_routers

api = NinjaAPI(title='API Мин Вода',auth=django_auth, csrf=True)

api.add_router("/tara/", taras_routers)
api.add_router("/country/", country_routers, tags=["Страны"])
api.add_router("/products/", products_routers, tags=["Продукты"])
api.add_router("/consumer-codes/", consumer_codes_routers, tags=["Потребительские коды"])
api.add_router("/group-codes/", group_codes_routers, tags=["Груповые коды"])

api.add_router("/korob/", korob_routers, tags=["Ящики"])