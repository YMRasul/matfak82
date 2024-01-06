from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(Student)
class StudentAllAdmin(admin.ModelAdmin):  # должень совпадат с модели Admin для админ панели
    list_display = ('id', 'title','birthday','content', 'get_html_photo','is_live') # список полей
    list_display_links = ('id', 'title')                            # поля которые мы можем кликнут
    search_fields = ('title',)                                      # поля для поиска
    save_on_top = True                                              # если True  наверху повторится кнопки
    #x Это функция для отображения миниатюра на админ панеле в место пути
    #x в list_display вместо 'photo' пропишем 'get_html_photo'
    fields = ('title','birthday','content','grp','photo','get_html_photo','is_live')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self,object):
        '''
        Возврашает HTML страницы Если существует путь к фотографии
        '''
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
