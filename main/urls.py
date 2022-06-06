from django.urls import path
import main.views as v

app_name = 'shop'

urlpatterns = [
    path('', v.view_home, name='home'),
]
