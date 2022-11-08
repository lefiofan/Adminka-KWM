from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/test")
def index(request):
    return {"hi": "ha"}