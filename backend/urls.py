from rest_framework import routers
from django.conf.urls import url
from .views import UserViewSet, RoomViewSet, MenuEntryViewSet, EnterRoom
from rest_framework_swagger.views import get_swagger_view
from . import views

app_name = "backend"

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'menuentrys', MenuEntryViewSet)

urlpatterns = [
        url(r'^$', get_swagger_view()),
        url(r'rooms/join', views.EnterRoom.as_view())
]

urlpatterns += router.urls
