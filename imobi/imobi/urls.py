# arquivo que defini as rotas da aplicaçaõ

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
