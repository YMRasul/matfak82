from django.contrib import admin
from django.urls import path,include
from apprasm.views import pageNotFound
from students import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apprasm.urls')),  # Создать файл urls.py в папке apprasm
    path('', include('appvideo.urls')),  # Создать файл urls.py в папке appvideo
    path('', include('appkurs.urls')),  # Создать файл urls.py в папке appkurs
    path('users/', include('appusers.urls',namespace='users')),  # Создать файл urls.py в папке appusers
    path("__debug__/", include("debug_toolbar.urls")),    # AAA
]

# Добавление  [***] от students.setttins
if settings.DEBUG:  # from students import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  для static    from django.conf.urls.static import static



handler404 = pageNotFound # обработчик для страницы 404
                          # функцию pageNotFound добавим в photo.views.py
