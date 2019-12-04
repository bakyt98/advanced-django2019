from django.contrib import admin

from auth_.models import MainUser, Profile
# Register your models here.
@admin.register(MainUser)
class MainUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login')
admin.site.register(Profile)
