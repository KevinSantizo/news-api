from django.contrib import admin
from news.models import New, NewCategory, CustomUser, Source
# Register your models here.


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


class NewCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


admin.site.register(New, NewAdmin)
admin.site.register(NewCategory, NewCategoryAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Source, SourceAdmin)
