from django.urls import path, include
from rest_framework import routers

from api import api_views as v

router = routers.DefaultRouter()
router.register(r'person', v.PersonListAPIView),

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
