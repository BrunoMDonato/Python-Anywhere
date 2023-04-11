from django.contrib import admin
from django.urls import path, include
from prueba1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('prueba1.urls'))

]

