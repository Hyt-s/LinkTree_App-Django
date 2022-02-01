from django.urls import path, include
from .views import LinkTreeMVS, LinksMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('linktree', LinkTreeMVS)
router.register('links', LinksMVS)

urlpatterns = [
    path('', include(router.urls))
]