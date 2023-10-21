from django.urls import path
from .views import(
    register_func,
    login_func,
    logout_view,
)

app_name = "account"

urlpatterns = [
   path('register/', register_func, name='register'),
   path('login/',login_func, name='login'),
   path('logout/', logout_view, name='logout'),
]
