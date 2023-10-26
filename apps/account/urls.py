from django.urls import path

from .views import(
    register_func,
    login_func,
    logout_func,
    profile_update_view,
    my_profile,
    
    
)

app_name = "account"

urlpatterns = [
   path('register/', register_func, name='register'),
   path('login/',login_func, name='login'),
   path('logout/', logout_func, name='logout'),
   path('profile/',my_profile, name= 'my_profile' ),
   path('profile/update/', profile_update_view, name = 'profile_update', )
   
]
