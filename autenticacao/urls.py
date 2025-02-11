from django.urls import path
from django.contrib import admin
from . import views  # Certifique-se de que há uma view no app

app_name = "autenticacao"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.login, name="login"),
    path("get_perfis/", views.get_perfis, name="get_perfis"),
    path("logout/", views.logout, name="logout"),
    # path('reservas/', include('reservas.urls')),
]
