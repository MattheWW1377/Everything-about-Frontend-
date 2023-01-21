from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main.views import index, demand, geography, skills, recent_vacancies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('demand/', demand, name='demand'),
    path('geography/', geography, name='geography'),
    path('skills/', skills, name='skills'),
    path('recent-vacancies/', recent_vacancies, name='recent_vacancies'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
