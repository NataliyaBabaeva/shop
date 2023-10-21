from django.contrib import admin



from .models import  User

# admin.site.register(UserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'pk','email']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['pk', 'username', 'email', 'first_name', 'last_name']
    


