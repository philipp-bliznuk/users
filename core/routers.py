from rest_framework import routers

from .viewsets import UserAccountViewSet


router = routers.SimpleRouter()
router.register(r'users', UserAccountViewSet)
